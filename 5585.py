money = 1000 - int(input())

change_money = [500, 100, 50, 10, 5, 1]

cnt = 0

for i in change_money:
    cnt += money//i
    money %= i

print(cnt)