ifconfig = """Link encap:Ethernet  HWaddr 00:1C:CX:AE:B5:E6
inet addr:192.168.0.1  Bcast:192.168.0.255  Mask:255.255.255.0
inet6 addr: fe80::21c:c0ff:feae:b5e6/64 Scope:Link
UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
RX packets:41620 errors:0 dropped:0 overruns:0 frame:0
TX packets:40231 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:21601203 (20.6 MiB)  TX bytes:6145876 (5.8 MiB)
Interrupt:21 Base address:0xe000 """

import re

def validateMacAddress(mac):
    x = mac.split(":")
    pattern = re.compile("[0-9a-fA-F]")
    if len(x) == 6:
        macAddr = "".join(x)
        for char in macAddr:
            if re.match(pattern, char):
                continue
            else:
                return False
        return True
    
def returnMacAddress(text):
    pattern = re.compile("\w\w:\w\w:.+")
    mac = re.findall(pattern,text)
    v = validateMacAddress(mac[0])
    print (v)

returnMacAddress(ifconfig)
