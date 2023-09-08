arr = [list(map(int,input().split())) for _ in range(3)]

sol_x = []
sol_y = []

for i in range(3):
    x = arr[i][0]
    y = arr[i][1]
    if x not in sol_x:
        sol_x.append(x)
    else:
        sol_x.remove(x)
    
    if y not in sol_y:
        sol_y.append(y)
    else:
        sol_y.remove(y)

print(*sol_x,*sol_y)