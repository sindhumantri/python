def sumOfDigits(word):
    ele = [e for e in word]
    digits = [int(d) for d in ele if d.isdigit()]
    return sum(digits)

def sumOfDigitsInString(string):
    words = string.split(" ")
    sumOfDigitsInAString = []
    for word in words:
        print (word)
        if word.isalnum() or word.isnumeric():
            sumOfDigitsInAString.append(sumOfDigits(word))
    print (sumOfDigitsInAString)

sumOfDigitsInString("134s34a 1f34fgh 45fg567hj 1111")
