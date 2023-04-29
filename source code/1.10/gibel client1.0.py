import time 
import mouse 
import keyboard
#UI
print("hello! is new clientfor minecraft development by gibel team ")
print("our functions are: ")
print("1.trigger bot")
print("1.auto walk")
print("start setting")
delay=float(input("enter time delay (0.00)"))
hotKeyTriger=(input("enter hotkey for triger mode (any key)"))
hotKeyAutoWalk=(input("enter hotkey for auto walk mode (any key)"))
waitWalk=int(input("enter time waitWalk (00)"))
hotKeyBind1 = (input("enter hotkey for BIND1 (any key)"))
bind1 = (input("enter bind1 (any words or commands)"))

isCliking = False
def clicker ():
    global isCliking
    isCliking = not isCliking
def aw ():
    keyboard.press("w")
    time.sleep(waitWalk)
    keyboard.release("w")
def bindfirst ():
    keyboard.write(bind1)

keyboard.add_hotkey(hotKeyTriger, clicker)
keyboard.add_hotkey(hotKeyAutoWalk, aw)
keyboard.add_hotkey(hotKeyBind1, bindfirst)
while True:
    if isCliking:
        print("start pushing (trigger bot[ON])")
        mouse.click(button= 'left')
        time.sleep(delay)