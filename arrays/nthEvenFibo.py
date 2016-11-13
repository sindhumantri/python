# Find nth even number in a given n number

def fibonacciNumbers(n):
	fibNum = []
	if n == 0 or n == 1:
		return n
	fibNum.append(0)
	fibNum.append(1)
	while n >= 2:
		fib = fibNum[-1] + fibNum[-2]
		fibNum.append(fib)
		n -= 1
	return fibNum

def nthevenFib(fibSeries, nthEven):
	res = fibonacciNumbers(fibSeries)
	evenFib = []
	for i in res:
		if i%2 == 0 and len(evenFib) <= nthEven:
			evenFib.append(i)
	return evenFib[-1]

res = nthevenFib(20, 3)
print(res)

print("-----nth even series in O(n)-------")

def nthEvenFibo(nthTerm):
	a = 0
	b = 1
	count = 0
	fibNum = 0
	while count < nthTerm:
		if a%2 == 0 and a != 0:
			count += 1
			fibNum = a
		fib = a + b
		a = b
		b = fib
	return fibNum
res = nthEvenFibo(3)
print(res)
