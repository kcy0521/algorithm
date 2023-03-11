n = int(input())
sol = []
a = list(input().split() for _ in range(n))

for i in a:
    if len(i) == 1:
        if i[0] == 'top':
            if not sol:
                print(-1)
            else:
                print(sol[-1])
        elif i[0] == 'size':
            print(len(sol))
        elif i[0] == 'empty':
            if not sol:
                print(1)
            else:
                print(0)
        elif i[0] == 'pop':
            if not sol:
                print(-1)
            else:
                print(sol[-1])
                sol.pop(-1)
    else:
        sol.append(i[1])
    
