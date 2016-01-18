def distanceBtw2Strings(string,str1,str2):

    str1Index = []
    
    str2Index = []
    
    words = string.split(" ")
    
    print (words)
    i = 0
    for word in words:
        if word == str1:
            str1Index.append(i)
        if word == str2:
            str2Index.append(i)
        i += 1
    result = [abs(x - y) for x in str1Index for y in str2Index]
    if str1 == str2:
        result = [abs(x - y) for x in str1Index for y in str2Index if x != y]
    if result:
        return min(result)
    return 0

string = "the quick the brown quick brown the frog"
print (distanceBtw2Strings(string, "quick", "quick"))
