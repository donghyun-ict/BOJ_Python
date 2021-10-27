T = int(input())

for i in range(T):
    R, S = input().split(' ')
    R = int(R)
    S = list(S.rstrip(''))
    for i in range(len(S)):
        print(S[i]*R, end='')
    print()