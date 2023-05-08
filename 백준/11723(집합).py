n = int(input())

S = []

for _ in range(n):
    x = list(input().split())

    if len(x) == 1:
        if x[0] == 'all':
            S = list(range(1, 21))  # int
        
        elif x[0] == 'empty':
            S = []

    elif len(x) == 2:
        num = int(x[1])
        if x[0] == 'add':
            if num not in S:
                S.append(num)

        elif x[0] == 'remove':
            if num in S:
                S.pop(S.index(num))

        elif x[0] == 'toggle':
            if num in S:
                S.pop(S.index(num))
            else:
                S.append(num)

        elif x[0] == 'check':
            if num in S:
             print('1')
            else:
             print('0')
