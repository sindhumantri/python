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


