from text2emotion import get_emotion
import pyttsx3
import json
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        female_voice_found = True
        break

def speak_emotion(audio):#speaks using this
    engine.say(audio)
    engine.runAndWait()

def violet_asking():
    try:
        with open("feelings.json", "r") as f:
            emotion_qns = json.load(f)
            key = random.choice(list(emotion_qns.keys()))
            question = emotion_qns[key]
            speak_emotion(question)
    except Exception as e:
        print("Something went wrong:",e)





def emotion_detector(query):
    if "bad day" in query.lower():
        return "Sad"
    try:
        emotion = get_emotion(query)
    except Exception as e:
        print(e)



    dominant_emotion=max(emotion,key=emotion.get)
    if all(value==0 for value in emotion.values()):
        return "neutral"
    return dominant_emotion

def emotion_speaker(emotion):
    if emotion == "Happy":
        try:
            with open("happy.json", "r") as f:
                tell_user=json.load(f)
                key=random.choice(list(tell_user.keys()))
                violet_feels=tell_user[key]
                print(violet_feels)
                speak_emotion(violet_feels)
        except Exception as e:
            print(e)


    elif emotion == "Sad":
        try:
            with open("sad.json", "r") as f:
                tell_user = json.load(f)
                key = random.choice(list(tell_user.keys()))
                violet_feels = tell_user[key]
                print(violet_feels)
                speak_emotion(violet_feels)
        except Exception as e:
            print(e)

    elif emotion == "Fear":
        try:
            with open("fear.json", "r") as f:
                tell_user = json.load(f)
                key = random.choice(list(tell_user.keys()))
                violet_feels = tell_user[key]
                print(violet_feels)
                speak_emotion(violet_feels)
        except Exception as e:
            print(e)


    elif emotion == "Angry":
        try:
            with open("anger.json", "r") as f:
                tell_user = json.load(f)
                key = random.choice(list(tell_user.keys()))
                violet_feels = tell_user[key]
                print(violet_feels)
                speak_emotion(violet_feels)
        except Exception as e:
            print(e)


    elif emotion == "Surprise":
        try:
            with open("surprise.json", "r") as f:
                tell_user = json.load(f)
                key = random.choice(list(tell_user.keys()))
                violet_feels = tell_user[key]
                print(violet_feels)
                speak_emotion(violet_feels)
        except Exception as e:
            print(e)





