import sys
input = sys.stdin.readline

N = int(input())
weight = [int(input()) for _ in range(N)]
weight.sort()
res = 0
for i in range(N):
    res = max(res, weight[i]*(N-i))
print(res)