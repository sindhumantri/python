import random
randomList = []
count = 0
while count < 5:
	x = []
	for i in range(1,6):
		res = random.randrange(1,65)
		if not res in x:
			x.append(res)
		else:
			print("Fake Lottery: %d" % res)
	if len(x) == 5:
		count += 1
		randomList.append(x)

print(randomList)
bonus_p = []
count = 0
while count < 5:
	x = random.randint(1,6)
	print(x)
	if not x in bonus_p:
		count += 1
		bonus_p.append(x)
	else:
		print("Fake")
x = zip(randomList, bonus_p)
for a,b in x:
	a.append(b)
	print(a)
