"""If there are equal number of odd and even numbers in array"""
def evenOddIndexes(arr):
    even = 1
    odd = 0
    while even < len(arr) and odd < len(arr):
        while even < len(arr) and arr[even] % 2 == 0:
            even += 2
        while odd < len(arr) and arr[odd] % 2 == 1:
            odd += 2
        if even < len(arr) and odd < len(arr):
            arr[odd],arr[even] = arr[even],arr[odd]
    return arr

print (evenOddIndexes([2,10,20,5,3,1,12,16,9,11]))
    
