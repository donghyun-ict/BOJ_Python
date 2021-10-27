S = list(input().rstrip(''))
alphabet = [0 for i in range(26)]

for i in range(len(S)):
    if(ord(S[i]) >= 97):
        alphabet[ord(S[i]) - 97] += 1
    else:
        alphabet[ord(S[i]) - 65] += 1

cnt = 0
cnt = alphabet.count(max(alphabet))

if (cnt == 1):
    print(chr(alphabet.index(max(alphabet))+65))
else:
    print('?')