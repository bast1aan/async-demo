import asyncio
import time
from asyncio import Future

from pantry import Egg, Bread, Coffee
from fridge import Juice, Ham

from devices import Toaster, Fryer, EggCooker

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

async def toast_bread(slices:int):
	with Toaster() as toaster:
		for slice in range(0, slices):
			toaster.do('Putting a slice of bread in the toaster')
		toaster.do('Start toasting...')
		await toaster.cook(seconds=4)
		Toast = Bread
		toaster.do('Remove toast from toaster')
		return Toast()

async def fry_ham(slices:int):
	with Fryer() as fryer:
		fryer.do(f'putting {slices} slices of ham in the pan')
		fryer.do('cooking first side of ham...')
		await fryer.cook(seconds=3)
		for slice in range(0, slices):
			fryer.do('flipping a slice of ham')
		fryer.do('cooking other side of ham...')
		await fryer.cook(seconds=3)
		fryer.do('put ham on plate')
		return Ham()

async def cook_eggs(how_many:int) -> Egg:
	with EggCooker() as egg_cooker:
		egg_cooker.do('Warming the egg cooker')
		await egg_cooker.cook(3)
		egg_cooker.do(f'cook {how_many} eggs')
		await egg_cooker.cook(3)
		egg_cooker.do('put eggs on plate')
		return Egg()


async def main():
	now = time.time()

	print('Put the egg cooker to work')
	future_eggs:Future[Egg] = asyncio.ensure_future(cook_eggs(how_many=2))

	print('Put the ham fryer to work')
	future_ham:Future[Ham] = asyncio.ensure_future(fry_ham(slices=3))

	print('Put the toaster to work')
	future_toast:Future[Bread] = asyncio.ensure_future(toast_bread(slices=2))

	cup:Coffee = pour_coffee()
	print('coffee is ready')

	oj:Juice = pour_orange_juice()
	print('Orange juice is ready')

	print('Waiting for the toast to be ready..')
	toast:Bread = await future_toast
	print('Toast is toasted!')

	apply_butter(toast)
	apply_jam(toast)
	print('Toast is ready!')

	print('Waiting for the ham to be ready..')
	ham:Ham = await future_ham
	print('Ham is ready!')

	print('Waiting for the eggs to be ready')
	eggs:Egg = await future_eggs
	print('eggs are ready!')


	print('Breakfest ready! in %s s' % int(round(time.time() - now)))

if __name__ == '__main__':
	asyncio.run(main())
