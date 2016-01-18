def firstAndLastOccurance(numbers):
    d = {}
    i = 0
    for num in numbers:
        if not num in d:
            d[num] = [i]
        else:
            d[num].append(i)
        i += 1
    for key, values in d.items():
        print ("first occurance = %d and last occurance = %d" % (values[0], values.pop()))


firstAndLastOccurance([1,2,3,3,4,4,5,5,5,5,6,7])
