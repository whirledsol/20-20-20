'''
20-20-20
A fork of https://github.com/Elliot-Potts/20-20-20.git
@author: whirledsol
@date: 2019-05-19

'''
import time, configparser, logging,random
import mouse,keyboard
from win10toast import ToastNotifier

def main():
    #global vars
    path_ini = "202020.ini"
    path_log = "202020.log"
    time_work_s = 60#20*60
    time_break_s = 5#25
    time_idle_s = 5#5*60
    icon = "icon.png"
    messages_break = ["You have worked for 20 minutes straight. Please look at something 20 feet away for 20 seconds.",
    "It's that time again to look away from the screen for 20 seconds.",
    "Do your eyes a favor and look at something 20 feet away.",
    "To prevent eye strain, please give your eyes a 20 second break.",
    "Good work! Remember to blink and look away from the computer for a while.",
    "Remember the 20-20-20 rule.","Take that well-deserved 20 second break."]
    messages_resume = ["Back to work!","Thank you for taking care of your eyes.","You may resume.","20 seconds has passed. Good job.","You're doing great! Time to get back to work."]

    #setup
    toaster = ToastNotifier()
    config = configparser.ConfigParser()
    logging.basicConfig(filename=path_log,filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%c',
                                level=logging.DEBUG)


    #start
    logging.info("202020 Start")
    timer_work_start = time.time()
    timer_last_active = time.time()
    def activityRefresh(e): 
        global timer_last_active
        timer_last_active = time.time()
    mouse.hook(activityRefresh)
    
    while True:
        timer_work_while = time.time()
        
        #if we have been idle for greater than threshold, keep starting timer in sync with while timer 
        if(timer_work_while - timer_last_active) >= time_idle_s:
            timer_work_start = time.time()
            time.sleep(0.1)
            print(("%s - %s") % (timer_work_while,timer_last_active))

        if timer_work_while - timer_work_start >= time_work_s:
            logging.info("Break Start")
            toaster.show_toast("202020",random.choice(messages_break),icon_path=icon,duration=10,threaded=True)
            #read from config every time        
            config.read(path_ini)

            #if intrusive == True: also block input
            intrusive = config['DEFAULT']['intrusive'] if ('intrusive' in config['DEFAULT'])  else  False
            logging.info(("intrusive=%s") % intrusive)
            if (intrusive):
                mouse.hook(mouseblock)
                keyboard.hook(keyboardblock, True)
                logging.info("Input Blocked.")
            timer_break_start = time.time()
            timer_break_while = time.time()
            while timer_break_while - timer_break_start < time_break_s:
                timer_break_while = time.time()
                
            if (intrusive):
                mouse.unhook(mouseblock)
                keyboard.unhook(keyboardblock)
                logging.info("Input Unblocked.")
            
            logging.info("Break End")
            toaster.show_toast("202020",random.choice(messages_resume),icon_path=icon,duration=20,threaded=True)
            timer_work_start = time.time()

def mouseblock(e):
    mouse.move(5,5,True)

def keyboardblock(e):
    pass


if __name__ == '__main__': main()