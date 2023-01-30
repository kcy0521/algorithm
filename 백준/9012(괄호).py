n = int(input())
for _ in range(n):
    arr = input()
    sol = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            sol.append(arr[i])
        else:
            if len(sol) == 0:
                cnt += 1
                break
            else:
                sol.pop()
    
    if len(sol) !=0:
        cnt += 1
    
    if cnt > 0:
        print('NO')
    else:
        print('YES')
    

        