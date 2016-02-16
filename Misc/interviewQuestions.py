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

