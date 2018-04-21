# Written by Elliot Potts

import time
import keyboard
import mouse
import win32api
import pyttsx3
import playsound

speech_engine = pyttsx3.init()
speech_engine.setProperty("rate", 200)
mainLoop_start_time = time.time()

print(" [+] The  tool has been started. Don't disturb this window now!")

while True:
    mainLoop_while_time = time.time()
    if round(mainLoop_while_time, 1) - round(mainLoop_start_time, 1) == 5:
        print(" [!] 20 minutes has passed!")
        playsound.playsound("alert.mp3")
        speech_engine.say("20 minutes has passed. Look at something 20 feet away, and do this for 20 seconds.")
        speech_engine.runAndWait()

        innerLoopTime = time.time()

        while True:
            innerLoopTime_2 = time.time()
            if round(innerLoopTime_2, 1) - round(innerLoopTime) == 8:
                print(" [+] 20 seconds has passed!")
                break
            else:
                print("Waiting 8 seconds...")

        mainLoop_start_time = time.time()
