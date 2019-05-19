# Written by Elliot Potts

import time
import keyboard
import mouse
import win32api
import msvcrt
import pyttsx3
from win10toast import ToastNotifier
import configparser
import logging



path_ini = "202020.ini"
path_log = "202020.log"
time_work_s = 20*60
time_break_s = 20
KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

messages_break = ["You have worked for 20 minutes straight. Please look at something 20 feet away for 20 seconds.","It's that time again to look away from the screen for 20 seconds.","Do your eyes a favor and look at something 20 feet away.","To prevent eye strain, please give your eyes a 20 second break.","Good work! Remember to blink and look away from the computer for a while.","Remember the 20-20-20 rule.","Take that well-deserved 20 second break."]
messages_resume = ["Back to work!","Thank you for taking care of your eyes.","You may resume.","20 seconds has passed. Good job.","You're doing great! Time to get back to work."]

toaster = ToastNotifier()
config = configparser.ConfigParser()
logging.basicConfig(filename=path_log,filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Running Urban Planning")

timer_work_start = time.time()

print("20-20-20 has been started. Don't give up!")

while True:
    timer_work_while = time.time()
    if round(timer_work_while, 1) - round(timer_work_start, 1) >= time_work_s:
        
        config.read(path_ini)

        #if intrusive == True: also block input
        intrusive = config['DEFAULT']['intrusive'] or False
        logging.info("Break Start")

        timer_break_start = time.time()
        innerLoopMousePos = None
        innerLoopKeyBlock = False

        while round(timer_break_while, 1) - round(timer_break_start) < time_break_s:
            timer_break_while = time.time()
            if innerLoopMousePos is None:
                innerLoopMousePos = mouse.get_position()
            else:
                mouse.move(innerLoopMousePos[0], innerLoopMousePos[1])
                if innerLoopKeyBlock is False:
                    for item in KEYS:
                        keyboard.remap_key(item, 'space')
                    innerLoopKeyBlock = True
                    logging.info("Blocked all keyboard and mouse entry!")

        logging.info("20 seconds has passed!")
        keyboard.unhook_all()
        innerLoopKeyBlock = False
        logging.info("Restored keyboard and mouse entry.")
        
        timer_work_start = time.time()

