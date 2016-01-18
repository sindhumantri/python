import re

numbers = "192.168.1.10 999.999.999.123 2222.5555.111111.666 111.33.22 255.255.255.255"
ipaddr = numbers.split(" ")
for addr in ipaddr:
    l = addr.split(".")
    valid_range = [str(i) for i in range(1,256)]
    valid_num = [ele for ele in l if ele in valid_range]
    if len(valid_num) == 4 and len(l) == 4:
        print (".".join(l))
