# install the module 'pyautogui' first if you haven't
# pip install pyautogui

import pyautogui, time

# open the place where you wnat to execute this within this 5 seconds of sleep

time.sleep(5)
f = open("textfile.txt", 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")