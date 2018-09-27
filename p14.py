import numpy as np
from progressbar import ProgressBar
Bar = ProgressBar()
res = list()


def seq(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


for i in Bar(range(1, 1000000)):
    count = 0
    n = i
    while(n != 1):
        n = seq(n)
        count += 1
    res.append(count)
print(np.argmax(np.array(res)))
