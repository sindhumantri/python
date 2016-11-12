#Given an array A[] and a number x, check for pair in A[] with sum as x

def insertionSort(arr):
	for i in range(1, len(arr)):
		j = i
		hole = arr[i]
		while j > 0 and arr[j-1] > hole:
			arr[j] = arr[j-1]
			j -= 1
		arr[j] = hole
	return arr

def findSumOfParis(arr, givenSum):
	new_arr = insertionSort(arr)
	sumPairs = []
	i = 0
	j = len(new_arr) - 1
	while i < j:
		if new_arr[i] + new_arr[j] == givenSum:
			sumPairs.append((new_arr[i], new_arr[j]))
			i += 1
			j -= 1
		elif new_arr[i] + new_arr[j] < givenSum:
			i += 1
		elif new_arr[i] + new_arr[j] > givenSum:
			j -= 1
		else:
			return 0
	return sumPairs


def findSumOfParisUsingHash(arr, givenSum):
	constant_max = 50
	hashMap = [0]* constant_max
	for i in range(len(arr)):
		temp = givenSum - arr[i]
		if temp >= 0 and hashMap[temp] == 1:
			print("sum of a paris is: {}, {}".format(temp, arr[i]))
		hashMap[arr[i]] == 1
		
l = [1, 4, 45, 6, 10, -8]
s = 16
print("----Using Sorting method------")
res = findSumOfParis(l, s)
print(res)
print("---Using hash function-----")
findSumOfParisUsingHash(l, s)

print(res)
