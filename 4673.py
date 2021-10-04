def d(n):
    S = n
    while (n != 0):
        S += n % 10
        n //= 10
    return S

res = []

for i in range(1, 10001):
    res.append(d(i))
    if i not in res:
        print(i)