from time import sleep

from pantry import Egg, Bread, Coffee
from fridge import Juice, Ham


def pour_coffee():
	print('Pouring coffee..')
	return Coffee()

def pour_orange_juice():
	print('Pouring orangje juice')
	return Juice()

def apply_jam(toast:Bread):
	print('Putting jam on the toast')

def apply_butter(toast:Bread):
	print('Putting butter on the toast')

def toast_bread(slices:int):
	for slice in range(0, slices):
		print('Putting a slice of bread in the toaster')
	print('Start toasting...')
	Toast = Bread
	sleep(3)
	print('Remove toast from toaster')
	return Toast()

def fry_ham(slices:int):
	print(f'putting {slices} slices of ham in the pan')
	print('cooking first side of ham...')
	sleep(3)
	for slice in range(0, slices):
		print('flipping a slice of bacon')
	print('cooking other side of ham...')
	sleep(3)
	print('put ham on plate')
	return Ham()

def fry_eggs(how_many:int) -> Egg:

	print('Warming the egg cooker')
	sleep(3)
	print(f'cracking {how_many} eggs')
	sleep(3)
	print('put eggs on plate')
	return Egg()

def make_coffee() -> Coffee:
	print('Brewing coffee')
	sleep(3)
	return Coffee()

if __name__ == '__main__':
	cup:Coffee = make_coffee()
	print('coffee is ready')

	eggs:Egg = fry_eggs(how_many=2)
	print('eggs are ready')

	ham:Ham = fry_ham(slices=3)
	print('Ham is ready')

	toast:Bread = toast_bread(slices=2)
	apply_butter(toast)
	apply_jam(toast)
	print('Toast is ready')

	oj:Juice = pour_orange_juice()
	print('Orange juice is ready')

	print('Breakfest ready!')

