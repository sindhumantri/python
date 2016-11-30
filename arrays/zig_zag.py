def zig_zag(arr):
  i = 0
  while i < len(arr)-2:
    if i%2 == 0:
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
      if arr[i] < arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    i += 1
  return arr

arr = [4,3,7,8,6,2,1]
res = zig_zag(arr)
print(res)
