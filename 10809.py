S = list(input().rstrip(''))
alphabet = [-1 for i in range(26)]

for i in range(len(S)):
    if(alphabet[ord(S[i])-97] == -1):
        alphabet[ord(S[i])-97] = i

print(*alphabet, sep=' ')