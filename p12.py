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


TRI = triangle()
for tri in TRI:
    if numDiv(tri) == 500:
        print(tri)
        break
