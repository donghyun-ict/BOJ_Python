N = int(input())

x = N
L = []
for i in range(2, N+1):
    while (x%i == 0):
        L.append(i)
        x = x//i
        if (x%i != 0):
            break

for i in range(len(L)):
    print(L[i])