from math import ceil, sqrt


def primGen(n):
    i = 3
    j = 1
    j_max = 2
    while j < n:
        if checkPrim(i):
            j_max = i
            j += 1
        i += 1
    return(j_max)


def checkPrim(p):
    for i in range(2, ceil(sqrt(p)) + 1, 1):  # falsch für 2, daher startwerte anpassen
        if p % i == 0:
            return False
    return True


print(primGen(10001))
