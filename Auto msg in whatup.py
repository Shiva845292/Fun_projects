import pywhatkit as w
import pyautogui
import time
from datetime import datetime
import os

pyautogui.FAILSAFE= False
now = datetime.now()
n=0
while True:
    time.sleep(30)
    print("slp is competed",now.minute)
    now = datetime.now()
    for i in range(100):
        pyautogui.moveTo(5,i*2)
    for k in range(3):
        pyautogui.press('shift')
        now = datetime.now()
        if now.hour==23 and now.minute==59:
            w.sendwhatmsg("+916302147301", 'ni8 code testing with lappy', 00, 00)
            n=1
            pyautogui.click(1050, 950)
            pyautogui.press("enter")
            print("PAssed")
            os.system("shutdown /s /t 100")
            time.sleep(50)
            break
    if n==1:
        print("Completed")
        break
    else:
        continue


