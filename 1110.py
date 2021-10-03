N = int(input())
i = N

cnt = 0
while True:
    j = (i // 10) + (i % 10)
    i = ((i % 10) * 10) + (j % 10)
    cnt += 1
    if (i == N):
        break
    
print(cnt)