dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()
cnt = 0

for c in S:
    for i, k in enumerate(dial):
        if(c in k):
            cnt += i + 3
            
print(cnt)