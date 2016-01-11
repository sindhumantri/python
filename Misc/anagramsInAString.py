def anagrams(string):
    d = {}
    words = string.split()
    for word in words:
        newStr = list(word)
        newStr.sort()
        s = "".join(newStr)
        if not s in d.keys():
            d[s] = 1
        else:
            d[s] += 1
    for key in d.keys():
        if d[key] > 1:
            print (key)

        
anagrams("car tree boy girl arc cherry chrrey")

"""output = cehrry
acr"""
