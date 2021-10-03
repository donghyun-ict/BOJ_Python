import sys
input = sys.stdin.readline

N = int(input())
lengh = list(map(int, input().split()))
cost = list(map(int, input().split()))

x = cost[0]
res = lengh[0] * x

for i in range(1, N-1):
    if (x > cost[i]):
        x = cost[i]
        res += lengh[i] * x
    else:
        res += lengh[i] * x

print(res)