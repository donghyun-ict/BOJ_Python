import sys
input = sys.stdin.readline

N = int(input())

pos = []
one = []
neg = []

for i in range(N):
    x = int(input())
    if (x > 1):
        pos.append(x)
    elif (x == 1):
        one.append(x)
    else:
        neg.append(x)

pos.sort()
neg.sort(reverse = True)

ans = 0

while (len(pos) >= 2):
    ans += pos.pop() * pos.pop()

while pos:
   ans += pos.pop()

while one:
    ans += one.pop()

while (len(neg) >= 2):
    ans += neg.pop() * neg.pop()

while neg:
    ans += neg.pop()

print(ans)