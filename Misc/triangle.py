def revTriangle(n):
    for j in range(1,n+1):
        print (" ".join([str(i+1) for i in range(n-j+1)]))

def triangle(n):
    for j in range(1,n+1):
        print (" ".join([str(i+1) for i in range(j)]))

def astrict(n):
    i = 1
    while i <= n:
        print (i * "*")
        i += 1
    n -= 1

def revAstrict(n):
    i = 0
    while i <= n:
        print ((n-i) * "*")
        i += 1


def astrict(n):
    i = 1
    while i <= n:
        print (i * "*")
        i += 1
    n -= 1


def triangle(n):
    for i in range(1,n+1):
        x = i
        l = []
        while i:
            l.append(str(x))
            i -= 1
        print (" ".join(l))

def revTriangle(n):
    while n:
        x = n
        l = []
        i = 0
        while i < x:
            l.append(str(x))
            i += 1
        print (" ".join(l))
        n -= 1

triangle(5)
print ()
revTriangle(5)
print ()
astrict(5)
print ()
revAstrict(5)
