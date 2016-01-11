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

def anagrams(string):
    d = {}
    words = string.split()
    for word in words:
        key = "".join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
            
    for key,val in d.items():
        if len(val) > 1:
            print (val)

anagrams("car tree boy girl arc cherry chrrey")

"""output = ['car', 'arc']
['cherry', 'chrrey']"""
