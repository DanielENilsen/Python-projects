
import random 
from random import randint 
from statistics import mode



"""Plotting a simple data for a store that wil find out when average custumer wil come to the store"""

class custumer:
	def __init__(self):		
		self.working = random.choice([True,False])
		self.car = random.choice([True,False])
		self.workhours_close = int(random.choice([14,15,16,17]))
		self.buy_time =  int(random.choice([10,11,12,13,14,15,16,17,18,19,20]))


class store:
	def __init__(self,storeOpen,storeClose):
		self.storeOpen = storeOpen
		self.storeClose = storeClose

 

def main():
	store_1 = store(10,20)
	custumer_work_array, car_array, custumer_dont_array, = [], [], [] 
	objs = [custumer()for i in range(1000)]
	for obj in objs:
		if obj.working == True and obj.workhours_close < obj.buy_time:custumer_work_array.append(obj.buy_time)
		elif obj.working == False:custumer_dont_array.append(obj.buy_time)
		if obj.car == True:car_array.append(obj.buy_time)

	work = mode(custumer_work_array)
	car = mode(car_array)
	dont_work = mode(custumer_dont_array)


	print("Most People that work like to go to the store",work)
	print("Most People that have car like to go to the store",car)
	print("Most People that don't work like to go to the store",dont_work)





	

main()






