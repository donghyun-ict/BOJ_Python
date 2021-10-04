C = int(input())

for i in range(C):
    L = list(map(int, input().split()))
    avg = (sum(L)-L[0])/L[0]
    cnt = 0
    for j in range(1, L[0]+1):
        if (L[j] > avg):
            cnt += 1
    res = (cnt/L[0]) * 100
    print('%.3f'% (res) + '%')