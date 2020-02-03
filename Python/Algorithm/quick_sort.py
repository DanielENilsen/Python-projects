from random import randint 


def create_randomNums(size=10,max=50):
	return [randint(0,max) for _ in range(size)]

"""" Create a function that return a array of random numbers"""


def quick_sort(data):
	dataLen = len(data)

	if dataLen <= 1:
		return data
	else:
		pivotNum = data.pop()

	lower_array ,greater_array = [] ,[] 

	for num in data:
		if num > pivotNum:greater_array.append(num)
		else:lower_array.append(num)
	
	return quick_sort(lower_array) + [pivotNum]  + quick_sort(greater_array)


if __name__ == "__main__":	
	temp = create_randomNums()
	print(temp)
	print(quick_sort(temp))




