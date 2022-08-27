from pyautogui import *
import pyautogui
import keyboard
from datetime import datetime
import win32api, win32con

if __name__=="__main__":
    print("\n----------Script Started----------")
    while True:
        if pyautogui.locateOnScreen("D:\\VisualStudio\Python\\Netflix-Skip-Intro\\skipintro.png",confidence=0.8) != None:
            pyautogui.leftClick(x=1797, y=956)
            now = datetime.now()
            print("Skipped Recap at : ",now.strftime("%H:%M:%S"))
        elif pyautogui.locateOnScreen("D:\\VisualStudio\\Python\\Netflix-Skip-Intro\\skiprecap.png",confidence=0.8) != None:
            pyautogui.leftClick(x=1797, y=956)
            now = datetime.now()
            print("Skipped Intro at : ",now.strftime("%H:%M:%S"))
        else:
            pass