import time

import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(1211, 1056)
time.sleep(5)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(763, 607)
time.sleep(10)
pyautogui.write('em yeu anh Thuan Hoang dep trai pro vip <3', interval=0.25)
pyautogui.click(1084, 805)