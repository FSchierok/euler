def fib(max):
    n0 = 2
    n1 = 1
    n2 = 0
    while (n2 + n1) < max:
        n2 = n1
        n1 = n0
        n0 = n2 + n1
        print(n0)
        yield n0


FIB = fib(4000000)
sum = 0
for i in FIB:
    if i % 2 == 0:
        sum += i
print(sum + 2)  # n0=2 wird sonst nicht beachtet
