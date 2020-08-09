import numpy as np


def triangle():
    num = 0
    i = 1
    while True:
        num += i
        i += 1
        yield num


def primeFak(n):
    primes = dict()
    for i in range(2, n+1):
        if n % i == 0:
            primes[i] = primes.get(i, 0) + 1
            rek = primeFak(int(n / i))
            for prime, cnt in rek.items():
                primes[prime] = primes.get(prime, 0) + cnt
            break
    return primes


def multPlusOne(arr):
    tmp = np.array(arr)
    tmp += 1
    return np.prod(tmp)

TRI = triangle()
for tri in TRI:
    primeDict = primeFak(tri)
    primes = list(primeDict.values())
    if multPlusOne(primes) >= 500:
        print(tri)
        break
