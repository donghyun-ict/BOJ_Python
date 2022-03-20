T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    l = [_ for _ in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            l[i] += l[i-1]
    print(l[n-1])