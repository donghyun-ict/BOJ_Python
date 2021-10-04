N = int(input())
for i in range(N):
    L = list(input().rstrip())
    res = 0
    x = 1
    for j in range(len(L)):
        if (L[j] == 'O'):
            res += x
            x += 1
        else:
            x = 1
    print(res)