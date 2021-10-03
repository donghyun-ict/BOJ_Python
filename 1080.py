N, M = map(int, input().split())

A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if (A[i][j] == 0):
                A[i][j] = 1
            else:
                A[i][j] = 0

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if(A[i][j] != B[i][j]):
            flip(i, j)
            cnt += 1

ans = True
for i in range(N):
    for j in range(M):
        if(A[i][j] != B[i][j]):
            ans = False

if ans:
    print(cnt)
else:
    print(-1)