import sys
input = sys.stdin.readline

T = int(input())
button = [300, 60, 10]

if (T%10):
    print(-1)
else:
    button_cnt = []
    for i in button:
        button_cnt.append(T//i)
        T %= i
    print(*button_cnt)