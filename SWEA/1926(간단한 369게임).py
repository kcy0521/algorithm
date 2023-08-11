N = int(input())

sol = []
for i in range(1,N+1):
    cnt = 0
    x = str(i)
    for j in range(len(x)):
        if x[j] == '3' or x[j] == '6' or x[j] =='9':
            cnt += 1
    
    if cnt != 0:
        sol.append('-'*cnt)
    else:
        sol.append(x)


print(*sol)