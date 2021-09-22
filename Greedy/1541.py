exp = input().split('-')

result = 0

for i in exp[0].split('+'):
    result += int(i)

for i in exp[1:]:
    result_minus = i.split('+')
    for j in result_minus:
        result -= int(j)

print(result)