import time
from typing import IO

def spinning_cursor():
	while True:
		for cursor in '|/-\\':
			yield cursor

def spin(to:IO, seconds:float):
	spinner = spinning_cursor()
	for i in range(int(round(seconds*10))):
		to.write(next(spinner))
		if i % 10:
			to.write('  %s' % (seconds-(i // 10)))
		to.flush()
		time.sleep(0.1)
		to.write('\b')
		if i % 10:
			to.write('\b' * 3)
	to.write('-  0')
