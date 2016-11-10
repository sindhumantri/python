# Find the 2 repeated elemets in array For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5

def repeatedEle(arr, size, repeatCount):
	dupArr = []
	for i in range(size+repeatCount):
		if not arr[i] in dupArr:
			dupArr.append(arr[i])
		else:
			print("Duplicate element in array is: {}".format(arr[i]))

repeatedEle([4,2,4,5,2,3,1], 5, 2)

# find the repeated elements in array using O(n)

def dupElements(arr):
	for i in range(len(arr)):
		if arr[abs(arr[i])] > 0:
			arr[abs(arr[i])] = -arr[abs(arr[i])]
		else:
			print("duplicate elements :{}".format(abs(arr[i])))

dupElements([1,6,6,3,2,4,5,3])
