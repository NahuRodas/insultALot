import datetime
import random
from playsound import playsound # run: pip install playsound (if not working run: pip3 install playsound==1.2.2)
from gpiozero import DistanceSensor
  

# ------------------------VARIABLES-------------------------
# 3 Sets of sounds for each time of the day, change it to the path of your sounds
soundsMorning = ["path/audio1.mp3","path/audio2.mp3", "path/audio3.mp3"]
soundsAfternoon = ["path/audio1.mp3","path/audio2.mp3", "path/audio3.mp3"]
soundsNight = ["path/audio1.mp3","path/audio2.mp3", "path/audio3.mp3"]

# Time variables
morning = datetime.time(7,1,0)
afternoon = datetime.time(11,1,0)
night = datetime.time(16,1,0)

currentTime = datetime.datetime.now().time()

# Ultra Sonic Sensor variables
ultrasonic = DistanceSensor(echo = 17, trigger = 4, threshold_distance = 0.5, max_distance=1) 


# ------------------------FUNCTIONS-------------------------
# Checks current time and return what time of the day is (0: morning - 1: afternoon - 2: night)
def checkingTime(_currentTime):
    if(_currentTime >= morning and _currentTime < afternoon):
        return 0
    elif(_currentTime >= afternoon and _currentTime < night):
        return 1
    else:
        return 2

# Plays random audio depending of the time
def playAudio():
    if(checkingTime(currentTime) == 0):
        playsound(random.choice(soundsMorning), block = True)
    elif(checkingTime(currentTime) == 1):
        playsound(random.choice(soundsAfternoon), block = True)
    else:
        playsound(random.choice(soundsNight), block = True)



# ------------------------MAIN PROGRAM-------------------------
ultrasonic.when_in_range = playAudio

while True:
    currentTime = datetime.datetime.now().time()
    ultrasonic.wait_for_in_range()