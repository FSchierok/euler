from tqdm import tqdm
def A051626(n):
    if isA003592(n):
        return 0
    else:
        lpow=1
        while True:
            for mpow in range(lpow-1, -1, -1):
                if (10**lpow-10**mpow) % n == 0:
                    return lpow-mpow
            lpow += 1

def isA003592(n):
    while(n % 2)==0:
        n = n/2
    while (n%5) == 0:
        n = n/5

    return n ==0
maxL = 0
d = 0
for i in tqdm(range(1,1001)):
    current = A051626(i)
    if current > maxL:
        maxL = current
        d = i
print(d)
