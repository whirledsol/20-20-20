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
        innerLoopMousePos = None

        while True:
            innerLoopTime_2 = time.time()
            if round(innerLoopTime_2, 1) - round(innerLoopTime) == 8:
                print(" [+] 20 seconds has passed!")
                playsound.playsound("success.mp3")
                speech_engine.say("20 seconds has passed. Good job.")
                speech_engine.runAndWait()
                break
            else:
                if innerLoopMousePos is None:
                    innerLoopMousePos = mouse.get_position()
                    # innerLoopMousePos = x, y = win32api.GetCursorPos()
                else:
                    print(innerLoopMousePos)

        mainLoop_start_time = time.time()
