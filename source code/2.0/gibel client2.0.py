import time 
import mouse 
import keyboard
from config import *
from funk import *
from gui import *
while True:
        isCliking = False
        keyboard.add_hotkey(hotKeycliker,setup_auto_cliker)
        keyboard.add_hotkey(hotKeyBind1, bindfirst)
        keyboard.add_hotkey(hotKeyTriger, trigg)
        while True:
            if isCliking:
                print("start pushing (clicker bot[ON])")
                mouse.click(button= 'left')
                time.sleep(delay)



