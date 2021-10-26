def H(n):
    cnt = 0
    for i in range(1, n+1):
        if(i <= 99):
            cnt += 1
        else:
            number = list(map(int, str(i)))
            if(number[0] - number[1] == number[1] - number[2]):
                cnt += 1
    print(cnt)

N = int(input())
H(N)