"""
today we will add a wikipedia thinker which means we let jarvis to know the wikipedia article for its information
"""
import datetime
import time
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
r = sr.Recognizer()

for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        female_voice_found = True
        break

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    with sr.Microphone() as source:
        print("Listening to your voice...")
        r.pause_threshold=1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio).lower()
        print(f"\nYou said: {query}\n")
        speak(query)
        return query

    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"

def call_assistant(call_word="violet"):
    with sr.Microphone() as source:
        print("initialize the assistant....please speak the code ")
        pause_threshold =1
        try:
            audio = r.listen(source,timeout=5)
        except sr.WaitTimeoutError:
            return None

    try:
        print("just a sec.....")
        query2=r.recognize_google(audio,language='en-in').lower()
        print(f"\nYou said: {query2}\n")
        return query2
    except:
        return None
def greetings():
    now=datetime.datetime.now()
    hour=now.hour
    if(0<=hour<12):
        speak("good morning christy.")
    elif(12<=hour<18):
        speak("good afternoon christy.")
    else:
        speak("good evening christy.")
    speak("i am violet. your personal assistant.")
    speak("how can i help you today?")
def search_summary(contxt,sentences):
    try:
        summary = wikipedia.summary(contxt, sentences=sentences)
        return summary
    except Exception as e:
        print("Something went wrong:",e)






try:
    while True:
        result = call_assistant()
        k=False
        count=0
        if result is not None and "violet" in result:
            while True:
                if count<1:
                    greetings()
                count+=1

                commander = command()
                if "wikipedia" in commander:
                    try:
                        contxt=commander.replace("wikipedia","")
                        speak(f"you said {commander}")
                        speak(" input how many sentence do you want?")
                        sentences = int(input("enter sentences no: "))
                        summary=search_summary(contxt,sentences)
                        speak(f"your summary is {summary}")
                        print(summary)
                    except Exception as e:
                        print("Something went wrong:",e)
                    time.sleep(1)



                if commander == "stop":
                    speak("ok you said stop. ")
                    speak("so see you again christy. ")
                    speak("and wishing you all the best with devika. ")
                    k=True
                    break
            time.sleep(1)
        if(k==True):
            break

        elif(result is None):
            speak("you are not saying any thing dear")
            time.sleep(2)#2 seconds
        elif result is not None:
            speak("say my name please")
            time.sleep(1)

except Exception as e:
    print("Something went wrong",e)
    speak("sorry.an error occured.")




