import re

x = [1,9,8, 4, 0, 0, 2, 7, 0, 6, 0]
y = "".join([(str(i)) for i in x])
substr = re.sub("0", "", y)
for i in range(len(y) - len(substr)):
    substr += "0"
if len(y) == len(substr):
    print ([int(i) for i in list(y)])
    print ([int(i) for i in list(substr)])


x = [1,9,8, 4, 0, 0, 2, 7, 0, 6, 0]
count = 0
for i in x:
    if i == 0:
        count += 1
for i in range(count):
    x.remove(0)
    x.append(0)
print (x)
