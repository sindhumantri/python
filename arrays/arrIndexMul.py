""" Given an array of integers, update the index with multiplication of previous and next integers,"""

res = []
arr = [2,3,4,5,6]
s = 0
e = len(arr)-1
for i in range(len(arr)):
	if i != s and i != e:
		m = arr[i-1] * arr[i+1]
		res.append(m)
	elif s == i and i+1 != 0:
		m = arr[i] * arr[i+1]
		res.append(m)
	elif e == i and i-1 != 0:
		m = arr[i-1] * arr[i]
		res.append(m)
print(res)
