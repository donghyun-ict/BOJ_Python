N = int(input())

word = []
for i in range(N):
    word.append(input())

alphabet = [0 for i in range(26)]
for w in word:
    i = 0
    while w:
        x = w[-1]
        alphabet[ord(x) - ord('A')] += pow(10, i)
        w = w[:-1]
        i += 1

alphabet.sort(reverse=True)

ans = 0
for i in range(10):
    ans += (9-i) * alphabet[i]

print(ans)