M, N = map(int, input().split())

check = [0] * (N + 1)

for i in range(2, N+1):
    if (check[i] == 0):
        if (i>=M):
            print(i)
        for j in range(i*2, N+1, i):
            if (check[j] == 0):
                check[j] = 1