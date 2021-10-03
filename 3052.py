A = []
for _ in range(10):
    A.append(int(input()))

for i in range(10):
    A[i] = A[i] % 42

A = set(A)
print(len(A))