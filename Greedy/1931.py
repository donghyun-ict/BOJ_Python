N = int(input())
meeting = [[[0] for j in range(2)] for i in range(N)]

for i in range(N):
    meeting[i] = list(map(int, input().split()))

meeting = sorted(meeting, key=lambda a:a[0])
meeting = sorted(meeting, key=lambda a:a[1])

end = 0
cnt = 0

for i, j in meeting:
    if (i >= end):
        end = j
        cnt += 1

print(cnt)