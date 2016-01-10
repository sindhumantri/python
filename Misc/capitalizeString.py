def capitalizesTheWord(mString, dnotString):
    words = mString
    if type(words) == str:
        words = mString.split()
    newString = ""
    for word in words:
        if word in dnotString:
            newString += " " + word
        else:
            newString += " " + word.capitalize()
    print (newString)
            
    
doNotList = ["a", "the", "to", "at", "in", "with", "and", "but", "or"]
capitalizesTheWord("i loVe solving pRoblemS and it is fun",doNotList)

"""output = I Love Solving Problems and It Is Fun"""
