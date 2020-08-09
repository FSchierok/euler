def d(n):
    def div(n):
        dividers = list()
        for i in range(2, n // 2 + 2):
            if n % i == 0:
                dividers.append(i)
        return dividers

    return sum(div(n)) + 1


amicable = list()
for i in range(1, 10001):
    a = d(i)
    if (d(a) == i) and (a != i) :
        amicable.append(a)

print(sum(amicable))
