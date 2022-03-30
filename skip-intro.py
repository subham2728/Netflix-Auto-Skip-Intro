from pyautogui import *
import pyautogui
import keyboard
from datetime import datetime
import win32api, win32con

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("\n----------Script Started----------")

while keyboard.is_pressed('x') == False:
    if pyautogui.locateOnScreen("skiprecap.png",confidence=0.8) != None:
        click(1275,676)
        print("Skipped Recap at : ",current_time)
    elif pyautogui.locateOnScreen("skipintro.png",confidence=0.8) != None:
        click(1275,676)
        print("Skipped Intro at : ",current_time)
    else:
        continue



