#check weather the given string is a palindrome or Not

def isPalindrome(string):
  flag = 1
  f = 0
  l = 1
  while f < len(string)-1 and l < len(string)-1:
    if string[f] != string[-l]:
      flag = 0
    f += 1
    l += 1
  if flag == 0:
    print("not a palindrome")
  else:
    print("palindrome")

isPalindrome("mada")
