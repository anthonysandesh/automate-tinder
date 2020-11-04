import pyautogui
import time

#put cursor on the location to click before running this code.
cursour_location = pyautogui.position() 

# >>> Point(x=1457, y=894)

i=0
while i < 10: #number of times to be clicked 
    pyautogui.click(cursour_location)
    speed.time(0.2)
    i += 1     
