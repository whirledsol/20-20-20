# Written by Elliot Potts

import time
import keyboard
import mouse
import win32api
import msvcrt
import pyttsx3
import playsound


speech_engine = pyttsx3.init()
speech_engine.setProperty("rate", 200)
mainLoop_start_time = time.time()

print(" [+] The  tool has been started. Don't give up!")

while True:
    mainLoop_while_time = time.time()
    if round(mainLoop_while_time, 1) - round(mainLoop_start_time, 1) == 1200:
        print(" [!] 20 minutes has passed!")
        playsound.playsound("alert.mp3")
        speech_engine.say("20 minutes has passed. Look at something 20 feet away, and do this for 20 seconds.")
        speech_engine.runAndWait()

        KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        innerLoopTime = time.time()
        innerLoopMousePos = None
        innerLoopKeyBlock = False

        while True:
            innerLoopTime_2 = time.time()
            if round(innerLoopTime_2, 1) - round(innerLoopTime) == 20:
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
                    # print("X = {}, Y = {}".format(str(innerLoopMousePos[0]), str(innerLoopMousePos[1])))
                    mouse.move(innerLoopMousePos[0], innerLoopMousePos[1])
                    if innerLoopKeyBlock is False:
                        for item in KEYS:
                            keyboard.remap_key(item, 'space')
                        innerLoopKeyBlock = True
                        print(" [!] Blocked all keyboard and mouse entry!")
        keyboard.unhook_all()
        print(" [+] Restored keyboard and mouse entry!"+("\n"*10))
        innerLoopKeyBlock = False

        mainLoop_start_time = time.time()
