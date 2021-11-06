X = int(input())

n = 1
level = 1

while (n <= X):
    n += level
    level += 1

a = n - X
b = X - n + level

if(level % 2 == 0):
    print('%d/%d'% (a, b))
else:
    print('%d/%d'% (b, a))