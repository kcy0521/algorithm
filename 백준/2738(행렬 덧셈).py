n, m = map(int, input().split())

arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]

sol = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        sol[i][j] =  arr1[i][j] + arr2[i][j]
    
for i in range(n):
    print(*sol[i])
