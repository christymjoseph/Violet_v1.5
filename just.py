import tkinter as tk
from tkinter import Canvas, Label
import pyaudio
import numpy as np
import threading
import time
import speech_recognition as sr

class VoiceVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Violet - Smart Voice Interface")
        self.root.geometry("800x400")
        self.root.configure(bg='#040f1a')

        self.canvas = Canvas(self.root, bg="#040f1a", width=800, height=250, highlightthickness=0)
        self.canvas.pack(pady=10)

        self.speech_label = Label(self.root, text="Listening...", font=("Consolas", 18), fg="#00ffff", bg="#040f1a")
        self.speech_label.pack(pady=10)

        self.wave_lines = [self.canvas.create_line(0, 125, 800, 125, fill="#00ffff", width=2, smooth=True) for _ in range(3)]

        self.running = True
        self.chunk = 512  # reduced chunk for faster updates
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.smoothed_volume = 0.1  # initial smoothing value

        threading.Thread(target=self.animate_waveform, daemon=True).start()
        threading.Thread(target=self.listen_and_display, daemon=True).start()

    def animate_waveform(self):
        phase_offsets = [0, 1, 2]
        smoothing_factor = 0.05
        while self.running:
            try:
                data = np.frombuffer(self.stream.read(self.chunk, exception_on_overflow=False), dtype=np.int16)
                raw_volume = np.abs(data).mean() / 1000.0
                raw_volume = max(0.05, min(raw_volume, 1.0))

                # Smooth volume
                self.smoothed_volume = self.smoothed_volume * (1 - smoothing_factor) + raw_volume * smoothing_factor

                for idx, line in enumerate(self.wave_lines):
                    points = []
                    for x in range(0, 800, 8):
                        y = 125 + np.sin(x * 0.025 + time.time() * 5 + phase_offsets[idx]) * 40 * self.smoothed_volume
                        points.append(x)
                        points.append(y)
                    self.canvas.coords(line, *points)
            except Exception as e:
                print("Waveform error:", e)

            self.canvas.update_idletasks()
            time.sleep(0.01)

    def listen_and_display(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.7)
            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=7)
                    query = self.recognizer.recognize_google(audio).strip()
                    print("You said:", query)
                    self.update_label(query)
                except Exception as e:
                    self.update_label("...")
                    print("Error or silence:", e)

    def update_label(self, text):
        self.speech_label.config(text=text)

    def stop(self):
        self.running = False
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceVisualizer(root)
    try:
        root.mainloop()
    finally:
        app.stop()
