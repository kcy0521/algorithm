def add(x):
    if x not in S:
        S.append(x)

def check(x):
    if x in S:
        a = S.index(x)
        S.pop(a)

n = int(input())

S = []
A = [input().split() for _ in range(n)]

for i in range(n):
    x = A[i][0]
    if x == 'add':
        add(A[i][1])
    elif x == 'remove':
        check(A[i][1])
    elif x == 'check':
        if A[i][1] in S:
            print(1)
        else:
            print(0)
    elif x == 'toggle':
        if A[i][1] in S:
          x = S.index(A[i][1])
          S.pop(x)
        else:
          S.append(A[i][1])
    elif x == 'all':
        S = list(range(1,21))
    
    elif x == 'empty':
        S = []
