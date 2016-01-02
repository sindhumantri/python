"""Maximum occurance of a char in string"""

str1 = "testsample"
str2 = "geeksforgeeks"

dictCount = {}
for ele in str1:
    if not ele in dictCount.keys():
        dictCount[ele] = 1
    else:
        dictCount[ele] += 1
        
for ele in str2:
    if not ele in dictCount.keys():
        dictCount[ele] = 1
    else:
        dictCount[ele] += 1

print (dictCount)
def func(dictCount):
    for key in dictCount.keys():
        #print (key)
        #print (dictCount[key])
        max = 0
        maxEle = ""
        if dictCount[key] > max:
            max = dictCount[key]
            maxEle += key
    print (maxEle)

func()
