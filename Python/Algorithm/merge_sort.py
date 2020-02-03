from random import randint 

def create_randomNums(size=10,max=50):
	return [randint(0,max) for _ in range(size)]

"""" Create a function that return a array of random numbers"""

def merge_sort(data):
	if len(data) > 1:
		mid = len(data) // 2 
		left_array = data[:mid]
		right_array = data[mid:]

		i = 0
		j = 0
		k = 0

		merge_sort(left_array)
		merge_sort(right_array)

		while len(left_array) > i and len(right_array) > j:
			if left_array[i] < right_array[j]:
				data[k] = left_array[i]
				i+=1
			else:
				data[k] = right_array[j]
				j+=1
			k+=1

		while len(left_array) > i:
			data[k] = left_array[i]
			i+=1
			k+=1

		while len(right_array) > j:
			data[k] = right_array[j]
			j+=1
			k+=1


def println(data):
	return print(data,end="\n")
		

if __name__ =="__main__":
	temp = create_randomNums()
	println(temp)
	merge_sort(temp)
	println(temp)

# random array =  [16, 12, 12, 48, 43, 31, 28, 37, 42, 29]
# now sorted   =  [12, 12, 16, 28, 29, 31, 37, 42, 43, 48]