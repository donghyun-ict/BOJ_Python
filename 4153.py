import sys
input = sys.stdin.readline

while True:
    L = list(map(int, input().split()))
    L.sort()
    if(L[2] == 0):
        break
    elif(L[0]**2 + L[1]**2 == L[2]**2):
        print('right')
    else:
        print('wrong')