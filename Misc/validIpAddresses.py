import re

numbers = "192.168.1.10 999.999.999.123 2222.5555.111111.666 111.33.22 255.255.255.255"
ipaddr = numbers.split(" ")
for addr in ipaddr:
    l = addr.split(".")
    valid_range = [str(i) for i in range(1,256)]
    valid_num = [ele for ele in l if ele in valid_range]
    if len(valid_num) == 4 and len(l) == 4:
        print (".".join(l))


# Another way of validating the address using ipaddress module
import re
from ipaddress import IPv4Network, IPv4Address, IPv4Interface

numbers = "192.168.1.10 999.999.999.123 2222.5555.111111.666 111.33.22 255.255.255.255"

def is_valid(ipaddress):
    ''' Checks if a IP address is valid '''
    try:
        IPv4Address(ipaddress)
        return True
    except ValueError:
        return False

addr = numbers.split(" ")
for a in addr:
	print(is_valid(a))
