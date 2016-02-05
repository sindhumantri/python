def QuickSort(arr,start,end):
    #print ("%s %d %d" % (arr,start,end))
    if start < end:
        pIndex = Partition(arr,start,end)
        #print ("Pivot index %d" %(pIndex))
        QuickSort(arr,start, pIndex-1)
        QuickSort(arr,pIndex+1, end)
    return (arr)

def Partition(arr,start,end):
    #print ("%s %d %d" % (arr,start,end))
    pivot = arr[end]
    #print (start)
    #print (end)
    pIndex = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[pIndex],arr[i] = arr[i],arr[pIndex]
            pIndex = pIndex+1
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return int(pIndex)

arr = [7,2,1,6,8,5,3,4]
print (QuickSort(arr,0,7))

