from time import sleep
from mouse import click
from keyboard import add_hotkey
from config import *
from funk import clicker, trigg, bindfirst

print("hello! is new clientfor minecraft development by gibel team ")
print("our functions are: ")
print("1.trigger bot")
print("2.bind")
print("3.clicker")

while True:
    isCliking = False
    clicker()

    trigg()

    bindfirst()

    keyboard.add_hotkey(hotKeycliker, clicker)
    keyboard.add_hotkey(hotKeyBind1, bindfirst)
    keyboard.add_hotkey(hotKeyTriger, trigg)
    while True:
        if isCliking:
            print("start pushing (clicker bot[ON])")
            mouse.click(button="left")
            time.sleep(delay)
