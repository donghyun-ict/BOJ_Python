T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    n = 1
    level = 1
    while True:
        if (n <= N):
            n += H
            level += 1
        else:
            a = N - H*(level-2)
            b = level-1
            if(b<=9):
                print(str(a)+'0'+str(b))
            else:
                print(str(a)+str(b))
            break