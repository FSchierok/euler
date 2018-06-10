def checkPalindrom(n):
    return str(n) == str(n)[::-1]


palis = list()
for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
        if checkPalindrom(i * j):
            palis.append(i * j)
print(max(palis))
