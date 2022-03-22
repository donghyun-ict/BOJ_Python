M = int(input())
N = int(input())

def prime_number(x):
    if (x < 2):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True
    
L = []
for i in range(M, N+1):
    if (prime_number(i) == True):
        L.append(i)
        
if (len(L)==0):
    print(-1)
else:
    print(sum(L))
    print(min(L))