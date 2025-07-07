import violet_emotions
TRIGGER_MAP = {
    # Create File Intents
    "create a file": "create_a_file",
    "make a new file": "create_a_file",
    "start a file": "create_a_file",
    "open a blank file": "create_a_file",
    "generate a file": "create_a_file",
    "start writing a file": "create_a_file",
    "prepare a file": "create_a_file",
    "set up a file": "create_a_file",
    "i want to create a file": "create_a_file",
    "make one file": "create_a_file",
    "new file please": "create_a_file",
    "make a file for me": "create_a_file",
    "initiate a file": "create_a_file",

    # Set Alarm Intents
    "set an alarm": "set_alarm",
    "wake me up at": "set_alarm",
    "remind me at": "set_alarm",
    "alarm for": "set_alarm",
    "i want to set an alarm": "set_alarm",
    "can you set an alarm": "set_alarm",
    "schedule an alarm": "set_alarm",
    "set a wake up call": "set_alarm",
    "create an alarm": "set_alarm",
    "make an alarm": "set_alarm",
    "ring me at": "set_alarm",
    "buzz me at": "set_alarm",
    "initiate alarm": "set_alarm",
    "start alarm": "set_alarm"
}


def intent_detect(query):
    query = query.lower()
    for trigger_phase,intent in TRIGGER_MAP.items():
        if trigger_phase in query:
            return intent

def intent_returner_with_mood(query):
    emotion=violet_emotions.emotion_detector(query)
    return [(emotion,intent_detect(query))]
