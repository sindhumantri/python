# find the elements ranging from 1 to 1000 and print all the numbers that are satisfying the following equation: x^2 + y^2 = z^2 and there should be no duplicate numbers

def gcd(a,b):
	while b!= 0:
		c = a%b
		a=b
		b=c
	return a

def pythagoreanThearem(n):
	for i in range(1, n+1):
		for j in range(i+1, n+1):
			if gcd(i,j) == 1:
				for k in range(j+1, n+1):
					if i*i + j*j == k*k:
						print("{}, {}, {}".format(i, j, k))

pythagoreanThearem(1000)
