"""Input:   str = "a,b$c"
Output:  str = "c,b$a"""

def reverseString(string):
  new_list = list(string)
  
  l = 0
  r = len(new_list) -1
  
  while l < r:
    if not new_list[l].isalpha():
      l += 1
    elif not new_list[r].isalpha():
      r -= 1
    else:
      new_list[l],new_list[r] = new_list[r], new_list[l]
      l += 1
      r -= 1
  return "".join(new_list)
  
res = reverseString("a!!!bb.c.d,e'f,ghi")
print(res)
