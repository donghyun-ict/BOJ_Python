N, K = map(int, input().split())

A = [0 for i in range(N)]

for i in range(N):
    A[i] = int(input())

A = sorted(A, reverse = True)

result = 0

for i in range(N):
    result += K // A[i]
    K %= A[i]

print(result)