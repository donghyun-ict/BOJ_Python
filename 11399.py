N = int(input())

P = list(map(int, input().split()))
P = sorted(P)

result = 0

for i in range(N):
    result += P[i] * (N - i)

print(result)