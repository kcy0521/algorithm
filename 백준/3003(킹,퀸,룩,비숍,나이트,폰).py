arr = list(map(int,input().split()))

check = [1,1,2,2,2,8]
sol = []
for i in range(len(arr)):
    x = check[i] - arr[i]
    sol.append(x)

print(*sol)


