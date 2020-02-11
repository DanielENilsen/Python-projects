import matplotlib.pyplot as plt 
import random 
from random import randint 
from statistics import mode


"""Plotting a simple data for a store that wil find out when average custumer wil come to the store"""

class custumer:
	def __init__(self):		
		self.working = random.choice([True,False])
		self.car = random.choice([True,False])
		self.buy_ours = []
		self.workhours_close = int(random.choice([14,15,16,17]))
		self.buy_time =  int(random.choice([14,15,16,17,18,19,20]))

class store:
	def __init__(self,storeOpen,storeClose):
		self.storeOpen = storeOpen
		self.storeClose = storeClose

 

	
def main():
	store_1 = store(10,20)
	custumer_work_array, car_array, custumer_dont_array, = [], [], [] 
	objs = [custumer()for i in range(10)]
	for obj in objs:
		if obj.working == True and obj.workhours_close < obj.buy_time:custumer_work_array.append(obj)
		elif obj.working == False:custumer_dont_array.append(obj)
		if obj.car == True:car_array.append(obj)

	zim = mode(custumer_work_array)
	print(zim)





"""
	data = [i.buy_time for i in custumer_work_array]
	data2 = [i.buy_time for i in custumer_dont_array]
	rageA = [i for i in range(len(data))]




	plt.scatter(data,rageA ,color = "r")	
	plt.show()


"""
main()






