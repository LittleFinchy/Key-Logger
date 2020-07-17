import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime


def on_press(key):
	print(key)

def on_release(key):
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()  fdsaf