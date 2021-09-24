import sys
input = sys.stdin.readline

S = int(input())

x = 0
i = 0

while (x <= S):
    i += 1
    x += i

print(i-1)