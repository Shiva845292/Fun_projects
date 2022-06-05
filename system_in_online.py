import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE= False
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
n=0
while n<60:
    time.sleep(120)
    print("slp is competed",n)
    now1 = datetime.now()
    for i in range(100):
        pyautogui.moveTo(5,i*2)
    for k in range(3):
        pyautogui.press('shift')
    n=n+1
print("Current Time =", current_time)
current_time1 = now1.strftime("%H:%M:%S")
print("Current Time =", current_time1)
print("completed Task")


