n = int(input())
arr = list(input().split() for _ in range(n))
sol = []

for i in arr:
    x = i[0]
    if len(i) == 1:
        if x == 'pop_front':
            if sol:
                print(sol[0])
                sol.pop(0)
            else:
                print(-1)
        elif x == 'pop_back':
            if sol:
                print(sol[-1])
                sol.pop(-1)
            else:
                print(-1)
        elif x == 'size':
            print(len(sol))
        elif x == 'empty':
            if not sol:
                print(1)
            else:
                print(0)
        elif x == 'front':
            if sol:
                print(sol[0])
            else:
                print(-1)
        elif x == 'back':
            if sol:
                print(sol[-1])
            else:
                print(-1)
        
    else: # 길이2
        if x == 'push_front':
            sol.insert(0, i[1])
        elif x == 'push_back':
            sol.append(i[1])