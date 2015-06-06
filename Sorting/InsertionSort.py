#! /usr/bin/python

def InsertionSort(listEle):
  for i in xrange(1, len(listEle)):
    val = listEle[i]
    j = i
    while((j > 0) and (listEle[j-1] > val)):
      listEle[j] = listEle[j-1]
      j = j -1
    listEle[j] = val

def main():
  listEle = [30, 20, 3, 1, 50, 60]
  InsertionSort(listEle)
  print listEle

if __name__ == "__main__":
  main()
