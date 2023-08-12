import os

# os.environ["DISPLAY"] = ":0"
# os.environ["XAUTHORITY"] = "/run/user/1000/gdm/Xauthority"

import pyautogui
import time

pyautogui.position()

pyautogui.moveTo(141, 429)
pyautogui.moveTo(141, 429, 2)

pyautogui.moveRel(0, 300, 2)
pyautogui.moveRel(300, 0, 2)

pyautogui.click()
pyautogui.click(clicks=2)  # 2번 클릭
pyautogui.clcik(clicks=2, interval=2)  # 2초 간격으로 2번 클릭

pyautogui.dobuleClick()

time.sleep(1)

pyautogui.typewrite(["a", "b", "c", "enter"])
