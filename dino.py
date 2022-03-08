import webbrowser
import keyboard
import time
import pyautogui
import threading
score = 0
x = 706                                                                           
webbrowser.open("https://trex-runner.com/")
#keyboard.press ('alt + tab')   
time.sleep(1)
keyboard.press("space") 
"""while True:
    print (pyautogui.position())
"""
def saut() :
    keyboard.press("space")

def add () :
    global x
    x +=1
    if x <= 720 :
        t = threading.Timer (1.4, add)    
        t.start()
    if x>= 720 :
        t= threading.Timer (5.0, add)
        t.start()

def check () :
    global x
    t = threading.Timer (15.0, add)    
    t.start()
    while True :
        ch1 = pyautogui.pixel(x, 622)
        ch2 = pyautogui.pixel (x, 575)
        ch3 = pyautogui.pixel (x, 600)
        if ch1 == (83, 83, 83)  :
            saut()
        elif ch2 == (83, 83, 83) :  
            saut()
        elif ch3 == (83, 83, 83) :
            saut()

check()

"""def check2 () :
    startx = 700
    starty = 570
    lst = []
    while True :
        for i in range (5) :
            for j in range (5) :
                lst.append (pyautogui.pixel(startx+i, starty+j))
        print (lst)
        for i in lst :
            if i != (247,247,247) :
                saut()

check2()"""

"""for i in range (40) : 
    pyautogui.moveTo(800, 600)
    keyboard.press("space")
    time.sleep (0.2)   """                       