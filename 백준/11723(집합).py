import sys
n = int(input())

S = []
Z = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

for _ in range(n):
    x = list(sys.stdin.readline().split())

    if x[0] == 'add':
        if x[1] not in S:
            S.append(x[1])

    elif x[0] == 'remove':
        if x[1] in S:
            S.pop(S.index(x[1]))

    elif x[0] == 'check':
        if x[1] in S:
            print('1')
        else:
            print('0')

    elif x[0] == 'toggle':
        if x[1] in S:
            S.pop(S.index(x[1]))
        else:
            S.append(x[1])

    elif x[0] == 'all':
        print(S)
        S = Z 
        print(S)
    elif x[0] == 'empty':
        S = []


