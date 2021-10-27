A, B = map(list, input().split())
A_temp = []
B_temp = []

for i in range(len(A)):
    A_temp.append(A[len(A)-i-1])
for i in range(len(B)):
    B_temp.append(B[len(B)-i-1])

A = "".join(A_temp)
B = "".join(B_temp)

print(max(A, B))