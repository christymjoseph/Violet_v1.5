import speech_recognition as sr
import  pyttsx3
def speak(query):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    # Print all available voices for debugging
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices):
        print(f"{i + 1}. ID: {voice.id} | Name: {voice.name} | Lang: {voice.languages}")
        # Try to set Zira or any female voice
    female_voice_found = False
    for voice in voices:
        if "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            print(f"\nSelected Voice: {voice.name} (ID: {voice.id})")
            female_voice_found = True
            break

    # Fallback to first available voice if Zira not found
    if not female_voice_found:
        print("\nWarning: Zira not found! Using default voice")
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('pitch', 1.7)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.9)

    engine.say("hello i am jarvis your personal assistant you said that   ")
    engine.runAndWait()
    engine.say(query)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f" You said: {query}\n")
        speak(query)
    except sr.UnknownValueError:
        print(" Sorry, I didn't catch that. Please repeat.")
        return "None"
    except sr.RequestError:
        print(" Could not request results from Google Speech Recognition service.")
        return "None"
    return query



# Run this only to test voice input
if __name__ == "__main__":
    take_command()

