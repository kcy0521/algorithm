n = int(input())
arr = list(input().split() for _ in range(n))
sol = []
for i in arr:
    if len(i) == 1:
        if i[0] =='pop':
            if sol:
                print(sol[0])
                sol.pop(0)
            else:
                print(-1)
        elif i[0] == 'size':
            print(len(sol))
        elif i[0] == 'empty':
            if not sol:
                print(1)
            else:
                print(0)
        elif i[0] == 'front':
            if sol:
                print(sol[0])
            else:
                print(-1)
        elif i[0] == 'back':
            if sol:
                print(sol[-1])
            else:
                print(-1)
    else:
        sol.append(i[1])