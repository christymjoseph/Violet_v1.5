import webbrowser
import os
import pywhatkit
import datetime
import time
import speech_recognition as sr
import pyttsx3
import wikipedia
from pip._internal import commands
from word2number import w2n
import subprocess

def system_app_opener(query):
    apps={
          "chrome":"C:\Program Files\Google\Chrome\Application\chrome.exe",
          "google":"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "brave":r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "notion":r"C:\Users\lenova\AppData\Local\Programs\Notion\Notion.exe",
        "calculator": "calc",
        "notepad": "notepad",
        "vs code": "code",
        "cmd": "cmd",
        "paint": "mspaint",
        "explorer": "explorer",
        "task manager": "taskmgr",
         "control panel": "control"

    }
    app_name=query.replace("open","").strip().lower()
    if app_name in apps:
       target=apps[app_name]
       try:
           subprocess.Popen([target])
           print(f"opening {app_name}")
       except Exception as e:
            print("Something went wrong:",e)
    else:
        print("app not found")




