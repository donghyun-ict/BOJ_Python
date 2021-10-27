N = int(input())
ans = N

for _ in range(N):
    S = input()
    for i in range(len(S)-1):
        if (S[i] == S[i+1]):
            pass
        elif (S[i] in S[i+1:]):
            ans -= 1
            break
print(ans)