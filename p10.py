from math import ceil, sqrt


def checkPrim(p):
    for i in range(2, ceil(sqrt(p)) + 1, 1):  # falsch für 2, daher startwerte anpassen
        if p % i == 0:
            return False
    return True


sum = 2
for i in range(3, 2000000, 1):
    if checkPrim(i):
        sum += i
print(sum)
