# Written by Elliot Potts

import time
import keyboard
import mouse
import win32api
import pyttsx3
import playsound

tool_start_time = time.time()

print(" [+] The  tool has been started. Don't disturb this window now!")

while True:
    loop_time = time.time()
    if round(loop_time, 1) - round(tool_start_time, 1) == 5:
        print(" [!] 20 minutes has passed!")
        playsound.playsound("alert.mp3")

