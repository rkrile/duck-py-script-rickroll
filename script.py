import os
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui
import random
import time

while True:
    # Move the mouse cursor randomly
    x_offset = random.randint(-20, 20)
    y_offset = random.randint(-20, 20)
    pyautogui.moveRel(x_offset, y_offset, duration=0.25)
    time.sleep(29)  # 29 second delay
