import time 
import mouse 
import keyboard
from config import *
#UI
print("hello! is new clientfor minecraft development by gibel team ")
print("our functions are: ")
print("1.trigger bot")
print("2.auto walk")
print("3.bind")
print("4.pvpmode(beta)")

isCliking = False
def clicker ():
    global isCliking
    isCliking = not isCliking
def aw ():
    keyboard.press("w")
    time.sleep(10000)
    keyboard.release("w")
def bindfirst ():
    keyboard.write(bind1)
def pvpmode ():
    keyboard.press("space")
    time.sleep(0.70)
    mouse.click(button= 'left')
    time.sleep(0.70)
    keyboard.release("space") 

keyboard.add_hotkey(hotKeyTriger, clicker)
keyboard.add_hotkey(hotKeyAutoWalk, aw)
keyboard.add_hotkey(hotKeyBind1, bindfirst)
keyboard.add_hotkey(hotKeypvp,pvpmode)
while True:
    if isCliking:
        print("start pushing (trigger bot[ON])")
        mouse.click(button= 'left')
        time.sleep(delay)