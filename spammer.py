import pyautogui, time

time.sleep(1)

f = open('text', 'r')

for word in f:
	time.sleep(5)
	pyautogui.typewrite(word)
	# pyautogui.press('enter')