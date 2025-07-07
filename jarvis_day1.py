import pyttsx3
#the initialisation of the python speech engine
friend=pyttsx3.init('sapi5')
#checks the rate 
rate=friend.getProperty('rate')
print(rate)
#checks the volume
curr_vol=friend.getProperty('volume')
percent=int(curr_vol)*100
friend.say(f"my current volume is {percent} percent.")
friend.runAndWait()


friend.say("devika will love you one day dear")
friend.runAndWait()
#set a new rate
friend.setProperty('rate',160)#slower
#speak with a new rate
friend.say("now i am speaking more slowly")
friend.runAndWait()
