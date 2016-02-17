"""Given a list of numbers [1,2,4,6,8,11,13,15,18,22] remove if adjacent numbers difference is 1"""

def removeAdjDiff(arr):
    i = 0
    deleteList = []
    while i < len(arr):
        if abs(arr[i] - arr[i+1]) == 1:
            arr.pop(i)
            arr.pop(i+1)
            i += 2
    print (arr)

removeAdjDiff([1,2,4,6,8,11,13,14,18,22])

listD = "10.0.0.1/8, 10.10.0.1/8, 10.0.10.1/8, 10.10.10.1/8"
newList = listD.split(",")
print (set(newList))


ListB = "34 56 45 98 23 45"
new = ListB.split(" ")
print (set(new))

def listNumbers(arr):
    for ele in arr:
        if arr.index(ele) == ele:
            print (ele)
            

listNumbers([1,2,3,3,4,6,6])

"""How to add + 13 to the given MAC address"""

macAddress = "0e:ab:2e:c4:de:fc"
def newMacAddress(address, num):
    x = address.split(":")
    y = "".join(x)
    "Converted Hex to Binary"
    hexToBinary = bin(int(y,16))[2:]
    binNum = bin(num)
    add = int(hexToBinary,2) + int(binNum,2)
    res = hex(add)[2:]
    if len(res) < 12 :
        x = '0' + res
    print (x)
    
    
newMacAddress(macAddress,13)


"""find the last IP in this subnet"""
Ip = "135.227.144.186/24"

import ipaddress
def lastValidIPAddress(ip):
    ip, subnet = ip.split("/")
    ipSplit = ip.split(".")
    ipSplit[3] = "0"
    networkAddr = ".".join(ipSplit)
    networkSubnetMask = networkAddr + "/" +subnet
    ipAddress = [str(x) for x in ipaddress.ip_network(networkSubnetMask).hosts()]
    print (ipAddress[-1])
    
lastValidIPAddress(Ip)


"""find the last IP in this subnet"""

def returnSubnetmask(subnet):
    x = ''
    if int(subnet) == 8:
        x = bin(0xff0000 << 8)
    elif int(subnet) == 16:
        x = bin(0xffff00 << 8)
    else:
        x = bin(0xffffff << 8)
    return list(x[2:])

def returnBinaryIpAddress(ipaddress):
    ip = ipaddress.split(".")
    #binaryIp = ''
    #for ele in ip:
     #   binaryIp += "{0:08b}".format(int(ele))
    return [int(x) for x in ip]
    
def lastValidIPAddress(ip):
    ipaddr, subnet = ip.split("/")
    netMask = returnSubnetmask(subnet)
    address = returnBinaryIpAddress(ipaddr)
    #print (netMask)
    #print (address)
    i = 0
    subnet = []
    while i < len(netMask):
        x = int("".join(netMask[i:i+8]),2)
        subnet.append(x)
        i += 8
    networkAddress = []
    for i in range(len(address)):
        y = subnet[i] & address[i]
        networkAddress.append(str(y))
    #print (address)
    #print (networkAddress)
    hosts = [str(i) for i in range(int(address[-1]), 255)]
    networkAddress[-1] = hosts[-1]
    print ("Valid ip address is: %s " % (".".join(networkAddress)))
    
    #print (networkAddress.rstrip("."))
    
        
    
Ip = "135.227.144.186/24"
lastValidIPAddress(Ip)




    
