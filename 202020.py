'''
20-20-20
A fork of https://github.com/Elliot-Potts/20-20-20.git
@author: whirledsol
@date: 2019-05-19

'''
import time, configparser, logging,random
import pyHook,pythoncom
from win10toast import ToastNotifier

def main():
    #global vars
    path_ini = "202020.ini"
    path_log = "202020.log"
    time_work_s = 10#20*60
    time_break_s = 8#25
    icon = ""
    messages_break = ["You have worked for 20 minutes straight. Please look at something 20 feet away for 20 seconds.","It's that time again to look away from the screen for 20 seconds.","Do your eyes a favor and look at something 20 feet away.","To prevent eye strain, please give your eyes a 20 second break.","Good work! Remember to blink and look away from the computer for a while.","Remember the 20-20-20 rule.","Take that well-deserved 20 second break."]
    messages_resume = ["Back to work!","Thank you for taking care of your eyes.","You may resume.","20 seconds has passed. Good job.","You're doing great! Time to get back to work."]

    #setup
    hm = pyHook.HookManager()
    toaster = ToastNotifier()
    config = configparser.ConfigParser()
    logging.basicConfig(filename=path_log,filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)


    #start
    logging.info("20-20-20 Start")
    while True:
        timer_work_start = time.time()
        timer_work_while = time.time()
        if timer_work_while - timer_work_start >= time_work_s:
            logging.info("Break Start")
            toaster.show_toast(random.choice(messages_break),icon_path=icon,duration=10)
            #read from config every time        
            config.read(path_ini)

            #if intrusive == True: also block input
            intrusive = config['DEFAULT']['intrusive'] or False
            logging.info(("intrusive=%s") % intrusive)
            if (intrusive):
                hm.MouseAll = block
                hm.KeyAll = block
                hm.HookMouse()
                hm.HookKeyboard()
                pythoncom.PumpMessages()
                logging.info("Input Blocked.")
            timer_break_start = time.time()
            timer_break_while = time.time()
            while timer_break_while - timer_break_start < time_break_s:
                timer_break_while = time.time()
                
            if (intrusive):
                hm.MouseAll = unblock
                hm.KeyAll = unblock
                hm.HookMouse()
                hm.HookKeyboard()
                pythoncom.PumpMessages()
                logging.info("Input Unblocked.")
            
            logging.info("Break End")
            toaster.show_toast(random.choice(messages_resume),icon_path=icon,duration=20)
            timer_work_start = time.time()

def block(e):
    return False

def unblock(e):
    return True

if __name__ == '__main__': main()