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
    x_offset = random.randint(-200, 200)
    y_offset = random.randint(-200, 200)
    pyautogui.moveRel(x_offset, y_offset, duration=0.25)
    time.sleep(40)  # 40 second delay, testing limits
