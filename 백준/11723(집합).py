n = int(input())

sol = []
arr = [input().split() for _ in range(n)]

for i in range(n):
    x = arr[i][0]
    y = arr[i][1]
    if x == 'add':
        if y not in sol:
            sol.append(y)
    elif x == 'remove':
        if y in sol:
            idx = sol.index(y)
            sol.pop(idx)
    elif x == 'check':
        if y in sol:
            print(1)
        else:
            print(0)
    elif x == 'toggle':
        if y in sol:
          idx = sol.index(y)
          sol.pop(idx)
        else:
          sol.append(y)
    elif x == 'all':
        sol = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',"17",'18','19','20']
    
    elif x == 'empty':
        sol = []
