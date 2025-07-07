import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(audio):

    voices = engine.getProperty('voices')
    female_voice_found = False
    for voice in voices:
        if "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)

            female_voice_found = True
            break

    engine.say(audio)
    engine.runAndWait()

def command():

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio).lower()
        print(f"\nYou said: {query}\n")
        speak(query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please repeat.")
        return "None"
    except sr.RequestError:
        print("Sorry, I cannot reach Google's servers right now.")
        return "None"

def call_assistant(call_word="violet"):
    with sr.Microphone() as source:
        print("listening to your command...")
        r.pause_threshold=1
        try:
            audio2 = r.listen(source,timeout=5)
        except sr.WaitTimeoutError:
            return None

    try:
        query2=r.recognize_google(audio2,language='en-in').lower()
        print(f"\nYou said: {query2}\n")
        return query2

    except :

        return None



# Call the function to test
while True:
    result = call_assistant()
    if result is not None and "violet" in result:
        speak("yes iam here")
        commander=command()
        if commander=="stop":
            speak("ok bye")
            break


    elif result is not  None: #quer2 can be anything
        speak("say my name please")





