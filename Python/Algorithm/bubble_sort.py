from random import randint 


def create_randomNums(size=10,max=50):
	return [randint(0,max) for _ in range(size)]

"""" Create a function that return a array of random numbers"""


def bubble_sort(data):
	for i in range(0,len(data) -1):
		for j in range(0,len(data) -1 -i ):
			if data[j] < data[j+1]:
				data[j] , data[j+1] = data[j+1] , data[j]
	return data 



if __name__ == "__main__":
	temp = create_randomNums()
	print(temp)
	print(bubble_sort(temp))

# random array  = [7, 45, 21, 31, 49, 12, 12, 42, 4, 14]
# now sorted    = [49, 45, 42, 31, 21, 14, 12, 12, 7, 4]
