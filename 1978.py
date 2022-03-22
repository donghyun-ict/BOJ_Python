N = int(input())
L = list(map(int, input().split()))

def prime_number(x):
    if (x < 2):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

cnt = 0
for i in range(N):
    if (prime_number(L[i]) == True):
        cnt += 1
        
print(cnt)