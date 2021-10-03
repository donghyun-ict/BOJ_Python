import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    applicant = []
    for i in range(N):
        paper, interview = map(int, input().split())
        applicant.append([paper, interview])
    applicant.sort()
    max = applicant[0][1]
    cnt = 1
    for i in range(1, N):
        if (max > applicant[i][1]):
            cnt += 1
            max = applicant[i][1]
    print(cnt)