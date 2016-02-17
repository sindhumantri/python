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




