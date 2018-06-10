#from progressbar import ProgressBar
from math import ceil, sqrt
#Bar = ProgressBar()
target = 600851475143


def primeFak(n):
    print(n)
    for i in range(2, ceil(sqrt(n)) + 1, 1):
        if n % i == 0:
            print("Fak:" + str(i))
            return(primeFak(n / i))


print(primeFak(target))
