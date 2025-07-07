import time
import datetime
import threading
speak_lock=threading.Lock()
import violet_time
import pyttsx3
import speech_recognition as sr
engine_time = pyttsx3.init('sapi5')
voices = engine_time.getProperty('voices')
r_time = sr.Recognizer()
for voice in voices:
    if "zira" in voice.name.lower():
        engine_time.setProperty('voice', voice.id)
        female_voice_found = True
        break

def speak_time(audio):#speaks using this
    engine_time.say(audio)
    engine_time.runAndWait()
def command_time(argument="listening to your voice........."):#gets the command to text and speaks can be used to get the speech and use it for other properties
    with sr.Microphone() as source:
        print(argument)
        r_time.adjust_for_ambient_noise(source,duration=0.8)
        r_time.pause_threshold=0.8
        r_time.energy_threshold=250

        try:
            audio = r_time.listen(source, timeout=15, phrase_time_limit=30)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            speak_time("I didn’t hear anything.")
            return "None"


    try:
        print("Recognizing...")
        query=r_time.recognize_google(audio).lower()
        print(f"\nYou said: {query}\n")
        query=query.strip().lower()
        speak_time(query)
        return query

    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"

alarms_list=[]
month_dict = {
    "january": 1, "jan": 1,
    "february": 2, "feb": 2,
    "march": 3, "mar": 3,
    "april": 4, "apr": 4,
    "may": 5,
    "june": 6, "jun": 6,
    "july": 7, "jul": 7,
    "august": 8, "aug": 8,
    "september": 9, "sep": 9, "sept": 9,
    "october": 10, "oct": 10,
    "november": 11, "nov": 11,
    "december": 12, "dec": 12
}


def add_alarms(time_str,label="ALARM"):
    try:
        alarm_time=datetime.datetime.strptime(time_str,"%Y-%m-%d %H:%M")
        alarms_list.append({"time":alarm_time , "label":label})
        print(f"alarm is set for {alarm_time}")
        speak_time(f"Alarm set for {time_str} with label {label}")


    except ValueError:
        print(" Invalid time format! Use YYYY-MM-DD HH:MM")

def check_alarms():
    while True:
        now=datetime.datetime.now().replace(second=0,microsecond=0)
        for alarm in alarms_list[:]:
            if now==alarm["time"]:
                speak_time(alarm["label"])
                #for future play music
                alarms_list.remove(alarm)
        time.sleep(10)
alarm_time_input=None
def alarm_loader():
    global alarm_time_input
    speak_time("please input alarm time as in the given format")
    alarm_time_input=input("please type in yyyy-mm-dd HH:MM :")
    speak_time("what should be the label for this alarm?")
    label=command_time("speak the label please")
    try:
        add_alarms(alarm_time_input,label)
    except ValueError:
        print("Invalid time format")
    except Exception as e:
        print(e)


threading.Thread(target=check_alarms,daemon=True).start()

print("[Violet Alarm] Alarm monitoring thread started.")
alarm_loader()











