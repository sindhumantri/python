def multiples(arr):
    mul = 1
    for i in arr:
        mul *= i
    return mul

def sumOfEleEqualToMultiples(arr):
    for i in range(len(arr)+1):
        for j in range(1, len(arr)+1):
            if sum(arr[i:j]) == multiples(arr[i:j]):
                print (arr[i:j])

sumOfEleEqualToMultiples([1,2,3,4,5])
