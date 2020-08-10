import numpy as np
from tqdm import tqdm


def isPrime(p):
    if p < 0:
        return False
    if p == 2:
        return True
    for i in range(2, (p // 2)+1):
        if (p % i) == 0:
            return False
    return True


def quad(a, b, n):
    return n ** 2 + a * n + b

primes = list()
for i in range(2,1001):
    if isPrime(i):
        primes.append(i)

print(isPrime(4))
maxL = 0
maxA = None
maxB = None
for a in tqdm(range(-999, 1000, 2)):
    for b in primes:
        for i in range(0, 1000):
            if not isPrime(quad(a, b, i)):
                if maxL < i:
                    maxL = i
                    maxA = a
                    maxB = b
                break
                print(quad(a,b,i))

for b in primes:
    for i in range(0, 1000):
       if not isPrime(quad(2, b, i)):
            if maxL < i:
                maxL = i
                maxA = 2
                maxB = b
            break
print(f"Lenght: {maxL}")
print(maxA, maxB)
print(maxA * maxB)
