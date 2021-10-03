A = int(input())
B = int(input())
C = int(input())

m = list(map(int, str(A * B * C)))
n = [0 for _ in range(10)]

for i in range(len(m)):
    n[m[i]] += 1

for i in range(10):
    print(n[i])