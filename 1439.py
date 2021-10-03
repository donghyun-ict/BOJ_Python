S = input()
S = list(map(int, S))

value = 0
for i in range(len(S) - 1):
    if (S[i] != S[i+1]):
        value += 1

ans = (value+1)//2
print(ans)