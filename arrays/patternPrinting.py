def printTriangle(n):
	for i in range(1,n+1):
		for j in range(1, i):
			print(i*j, end = "\t")
		print("\n")

printTriangle(4)

print("---Printing * in reverse triangle-------")

for i in range(5, 0, -1):
	print("*" * i)
	
print("\n".join(i * "*" for i in range(10, 0, -1)))

print("---Printing * in triangle-------")

for i in range(1, 5):
	print("*" * i)
	
print("\n".join(i * "*" for i in range(1, 5)))

for i in range(1,6):
	for j in range(i):
		print(i, end="\t")
	print("\n")

n = 0
for i in range(1,5):
	for j in range(i):
		n += 1
		print(n, end=" ")
	print("\n")

for i in range(1, 11):
	for j in range(11-i):
		print(" ", end = " ")
	for j in range(1, i):
		print(j, end=" ")
	for i in range(i, 0, -1):
		print(i, end= " ")
	print("\n")

	

