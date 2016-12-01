#Convert given digit into words

def getDigits(num):
  l = []
  i = 0
  while num:
    digit = num % 10
    num = int(num / 10)
    l.append((digit, i+1))
    i += 1
  return l[::-1]

def convertToWords(arr):
  ones = {1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
  tens = {10: "ten", 20: "twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90: "ninty", 100:"hundered and"}
  teens = {11: "leven", 12:"towelve", 13: "thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17: "seventeen", 18:"eighteen", 19:"ninteen"}
  string = ""
  for i in arr:
    d, index = i
    if index == 3:
      string += ones[d] + " " + tens[100] + " "
    if index == 2:
      n = int(str(d) + "0")
      string += tens[n] + " "
    if index == 1:
      string += ones[d]
  return string
  
arr = getDigits(532)
res = convertToWords(arr)
print(res)
  
