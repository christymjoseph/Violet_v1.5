import datetime
import threading
import time

violet_time=None

def time_producer():
    global violet_time
    while True:
        violet_time = datetime.datetime.now()
        time.sleep(1)

def get_time():
    if violet_time:
        return violet_time.strftime("%I:%M:%S %p")
    else:
        return "time is not available"

def get_raw_time():
    if violet_time:
        return violet_time

def violet_clock_starter():
    clock_thread=threading.Thread(target=time_producer,daemon=True)
    clock_thread.start()

