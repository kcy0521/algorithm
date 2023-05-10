n = int(input())
sol = []

for i in range(n):
    a = list(input().split())
    if len(a) == 1:
        x = a[1]
        if a[0] == 'add':
            if x not in sol:
                sol.append(x)
        elif a[0] == 'remove':
            if x in sol:
                sol.pop(sol.index(x))
            
        elif a[0] == 'check':
            if x in sol:
                print(1)
            else:
                print(0) 
        elif a[0] == 'toggle':
            if x not in sol:
                sol.append(x)
            else:
                sol.append(x)
    else: 
        # all and empty
        if a[0] == 'all':
            sol = [range(1,21)]
        elif a[0] == 'empty':    
            sol = []
            