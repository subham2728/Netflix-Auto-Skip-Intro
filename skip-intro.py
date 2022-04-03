from pyautogui import *
import pyautogui
import keyboard
from datetime import datetime
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

if __name__ == "__main__":
    print("\n----------Script Started----------")
    while keyboard.is_pressed('x') == False:
        if pyautogui.locateOnScreen("E:\\VisualStudio\\Python\\Netflix-Skip-Intro\\skiprecap.png",confidence=0.8) != None:
            click(1275,676)
            now = datetime.now()
            print("Skipped Recap at : ",now.strftime("%H:%M:%S"))
        elif pyautogui.locateOnScreen("E:\\VisualStudio\\Python\\Netflix-Skip-Intro\\skipintro.png",confidence=0.8) != None:
            click(1275,676)
            now = datetime.now()
            print("Skipped Intro at : ",now.strftime("%H:%M:%S"))
        else:
            pass



