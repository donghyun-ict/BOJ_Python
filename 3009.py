X = []
Y = []

def least_frequent(data):
    return min(data, key=data.count)

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

print(least_frequent(X), least_frequent(Y))