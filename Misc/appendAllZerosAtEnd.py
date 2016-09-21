import re

x = [1,9,8, 4, 0, 0, 2, 7, 0, 6, 0]
y = "".join([(str(i)) for i in x])
substr = re.sub("0", "", y)
for i in range(len(y) - len(substr)):
    substr += "0"
if len(y) == len(substr):
    print ([int(i) for i in list(y)])
    print ([int(i) for i in list(substr)])


temp = []
i = 0
count = 0
while i < len(x):
	if x[i] != 0:
		temp.append(x[i])
	else:
		count += 1
	i += 1

res = temp + [0]*4
print(res)

x = [1,9,8, 4, 0, 0, 2, 7, 0, 6, 0]
count = 0
for i in x:
    if i == 0:
        count += 1
for i in range(count):
    x.remove(0)
    x.append(0)
print (x)
