L = ['c=','c-','dz=','d-','lj','nj','s=','z=']

S = input()

for i in L:
    S = S.replace(i, '0')

print(len(S))