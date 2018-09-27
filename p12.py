def triangle():
    num = 0
    i = 1
    while True:
        num += i
        i += 1
        yield num


def numDiv(n):
    count = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            count += 1
    return count


def numDiv2(n):
    prims = [2, 3, 5, 7, 11, 13, 17, 19]
    exp = list()
    for prim in prims:
        i = 0
        if n % prim**i == 0:
            i += 1
        else:
            exp.append(i - 1)
    return("??")
# Binom: n über i ist anzahl um i aus n zu ziehen
# summe der Eponenten für alle Teiler aus einer Primzahl, + Binom von zahl der Primzahlen über 1-Zahl + Mischterme mit potenzen


TRI = triangle()
for tri in TRI:
    if numDiv(tri) == 500:
        print(tri)
        break
