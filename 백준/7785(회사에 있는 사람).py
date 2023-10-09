n = int(input())

arr = list(input().split() for _ in range(n))

sol = []

# 현재 출근중인 사람 확인하기 
for i in range(n):
    if arr[i][1] == 'enter':
        sol.append(arr[i][0])
    else:
        sol.remove(arr[i][0])

sol.sort(reverse=True)
print(*sol) 


