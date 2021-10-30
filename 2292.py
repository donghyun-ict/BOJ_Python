N = int(input())

cnt = 1
bee = 1

while (N > bee):
    bee += 6*cnt
    cnt += 1

print(cnt)