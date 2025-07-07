import json
import pyttsx3

import speech_recognition as sr2
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
r_JSON = sr2.Recognizer();
for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        female_voice_found = True
        break
def speak_JSON(audio):#speaks using this
    engine.say(audio)
    engine.runAndWait()
def command_JSON(argument="listening to your voice........."):#gets the command to text and speaks can be used to get the speech and use it for other properties
    with sr2.Microphone() as source:
        print(argument)
        r_JSON.adjust_for_ambient_noise(source,duration=0.8)
        r_JSON.pause_threshold=0.8
        r_JSON.energy_threshold=250

        try:
            audio = r_JSON.listen(source, timeout=15, phrase_time_limit=30)
        except sr2.WaitTimeoutError:
            print("Listening timed out.")
            speak_JSON("I didn’t hear anything.")
            return "None"


    try:
        print("Recognizing...")
        query=r_JSON.recognize_google(audio).lower()
        print(f"\nYou said: {query}\n")
        query=query.strip().lower()
        speak_JSON(query)
        return query

    except sr2.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr2.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"

def remember_JSON_FILE(key,value,file):
    speak_JSON(f"can i save {key} to this {file}")

    k=0
    while k<4:
        reply_JSON = command_JSON("listening to your save request...........").lower()
        k=k+1
        yes_variants = ["yes", "yeah", "yep", "sure", "ok", "okay", "affirmative"]
        if any(word in reply_JSON for word in yes_variants):
            speak_JSON("you said yes")
            try:
                try:
                    with open(file, "r") as f:
                        data = json.load(f)


                except FileNotFoundError:
                    data = {}  # if file not found then start fresh
                # add the data to the JSON FILE
                data[key] = value

                with open(file, "w") as f:
                    json.dump(data, f, indent=4)
                print(f"Saved successfully to {file}")
                speak_JSON(f"saved successfully to {file}")
                return
            except Exception as e:
                print(e)
        elif "no" in reply_JSON:
            speak_JSON("you said no")
            speak_JSON("hence i wont save this")
            return

def decider_filter_JSON(query):
    remember_words={   "remember that",
        "note that",
        "save that",
        "store that",
        "log that",
        "record that",
        "write this down",
        "keep this in memory"}
    key_words = {
        "name",
        "age",
        "goal",
        "mood",
        "favorite_color",
        "favorite_food",
        "hobby",
        "wake_up_time",
        "sleep_time",
        "birthday",
        "location",
        "language",
        "voice_type",
        "task_list",
        "reminders",
        "notes",
        "friends",
        "family",
        "college",
        "project",
        "dream",
        "motivation_quote",
        "achievement",
        "todo",
        "schedule",
        "emotion_memory",
        "recent_commands"
    }
    #filter sub module
    pri_filt_query=None
    sec_filt_query=None
    JSON_key=None

    for JSON_trigger in remember_words:
        try:
            if JSON_trigger.lower() in query:
                pri_filt_query = query.lower().replace(JSON_trigger.lower(), "").strip()
                break
        except Exception as e:
            print(e)
            return None
    if pri_filt_query is None:
        print("No memory trigger found.")
        return
    for key in key_words:
      try:
          if key.lower() in pri_filt_query:
              sec_filt_query = pri_filt_query.replace(f"my {key} is", "").strip()
              JSON_key = key
              break
      except Exception as e:
          print(e)
          return None
            #decider sub module
    if key in("name","age","goal","dream"):
        try:
            remember_JSON_FILE(JSON_key, sec_filt_query, "creator.json")
        except Exception as e:
            print(e)


def JSON_reader(key,file):
    try:
        with open(file, "r") as f:
            data = json.load(f)
            print(f"your {key} is {data[key]}")
            speak_JSON(f"your {key} is {data[key]}")
    except Exception as e:
        print(e)

def JSON_query_filter(query):
    user_query_creator = [
        "what is my", "what was my", "what are my", "what do", "what does",
        "who is my", "who was my", "who are my", "who were my",
        "where is my", "where are my", "where was my", "where were my",
        "when is my", "when was my", "when did my",
        "why is my", "why are my", "why did my",
        "how is my", "how are my", "how to my", "how do my", "how can my"
    ]
    key_words = [
        "name",
        "age",
        "goal",
        "mood",
        "favorite_color",
        "favorite_food",
        "hobby",
        "wake_up_time",
        "sleep_time",
        "birthday",
        "location",
        "language",
        "voice_type",
        "task_list",
        "reminders",
        "notes",
        "friends",
        "family",
        "college",
        "project",
        "dream",
        "motivation_quote",
        "achievement",
        "todo",
        "schedule",
        "emotion_memory",
        "recent_commands"
    ]
    JSON_key_of_creator = None
    for key in key_words:
        try:
            if key.lower() in query:
                JSON_key_of_creator = key
                break
        except Exception as e:
            print(e)
            return None
    if JSON_key_of_creator is None:
        print("no memory")
        return
    if(JSON_key_of_creator in ("name","age","goal","dream")):
        JSON_reader(JSON_key_of_creator,"creator.json")

def JSON_reader_check(query):
    user_query_creator = [
        "what is my", "what was my", "what are my", "what do", "what does",
        "who is my", "who was my", "who are my", "who were my",
        "where is my", "where are my", "where was my", "where were my",
        "when is my", "when was my", "when did my",
        "why is my", "why are my", "why did my",
        "how is my", "how are my", "how to my", "how do my", "how can my"
    ]
    for user_query in user_query_creator:
        try:
            if user_query.lower() in query:
                return True
        except Exception as e:
            print(e)
    return False



