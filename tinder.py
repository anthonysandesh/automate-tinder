import pyautogui
import time

cursour_location = pyautogui.position()
# >>> Point(x=1457, y=894)

i=0
while i < 10:
    pyautogui.click(cursour_location)
    speed.time(0.2)
    i += 1     