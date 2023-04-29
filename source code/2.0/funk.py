import time 
import mouse 
import keyboard
from config import *
def setup_auto_cliker():
    global isCliking
    isCliking = not isCliking
def bindfirst ():
    keyboard.write(bind1)
def trigg ():
    import mouse
    import datetime
    import numpy as np
    import cv2
    import pyautogui
    import os

    # Define the region of interest
    x, y, width, height = 675, 370, 150, 150

    # Get the first frame
    prev_frame = cv2.cvtColor(np.array(pyautogui.screenshot(region=(x, y, width, height))), cv2.COLOR_BGR2GRAY)

    while True:
        # Get the current frame
        curr_frame = cv2.cvtColor(np.array(pyautogui.screenshot(region=(x, y, width, height))), cv2.COLOR_BGR2GRAY)

        # Calculate the absolute difference between frames
        diff = cv2.absdiff(curr_frame, prev_frame)

        # Threshold the difference image
        threshold = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)[1]

        # Count the number of non-zero pixels in the threshold image
        count = cv2.countNonZero(threshold)

        # If there are changes, print a message
        if count > 0:
            mouse.click(button= 'left')
            print(f"{datetime.datetime.now()} - Change detected: {count} pixels")
        # Set the current frame as previous frame for the next iteration
        prev_frame = curr_frame

        # Capture the image in the given screen area
        img_gray = cv2.cvtColor(np.array(pyautogui.screenshot(region=(675, 370, 50, 50))), cv2.COLOR_RGB2GRAY)

        # Apply Gaussian blur to smooth out the image
        blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)

        # Show the results on the screen
        cv2.imshow('cheat vision', blurred)

        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    # Start the process as a background process
    os.system("trigg.py")
