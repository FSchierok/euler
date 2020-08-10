from tqdm import tqdm
def div(n):
    dividers = list()
    for i in range(2, n // 2 + 2):
        if n % i == 0:
            dividers.append(i)
    return dividers


abundant = list()

for i in tqdm(range(1, 28124)):
    if sum(div(i)) > i:
        abundant.append(i)

print("Abundant fertig")

NotSumOfAb = list()
for i in tqdm(range(1, 28124)):
    seen = False
    for j in abundant:
        if (i-j) > 0:
            if (i - j) in abundant :
                seen = True
                break
    if not seen:
        NotSumOfAb.append(i)
print(sum(NotSumOfAb))
