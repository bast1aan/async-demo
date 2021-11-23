from contextlib import contextmanager
from typing import IO, ContextManager

from spinner_file import spin


class Device:
	def __init__(self, f:IO):
		self.f = f
	def do(self, msg:str):
		self.f.write(msg)
		self.f.write('\n')
		self.f.flush()
	def cook(self, seconds:float):
		spin(self.f, seconds)
		self.f.write('\n')


@contextmanager
def Toaster() -> ContextManager[Device]:
	with open('/tmp/toaster.log', 'a') as f:
		device = Device(f)
		yield device

@contextmanager
def Fryer() -> ContextManager[Device]:
	with open('/tmp/fryer.log', 'a') as f:
		device = Device(f)
		yield device

@contextmanager
def EggCooker() -> ContextManager[Device]:
	with open('/tmp/egg_cooker.log', 'a') as f:
		device = Device(f)
		yield device
