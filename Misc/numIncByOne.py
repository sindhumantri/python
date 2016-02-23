def incByOne(num):
    x = list(str(num))
    carry = str(int(x[-1]) + 1)
    newCarry = 0
    newNum = []
    if len(carry) == 1:
        newNum.append("".join(x[:len(x)-1]))
        newNum.append(carry)
    elif len(x) == 1:
        newNum.append(str(num + 1))
    return int("".join(newNum))

print (incByOne(120))
