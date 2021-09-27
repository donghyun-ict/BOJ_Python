import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split())
    if (L+P+V == 0):
        break
    ans = L * (V // P) + min((V % P), L)
    print("Case %d: %d"% (i, ans))
    i += 1