n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n):
    for j in range(m):
        sol = list(map(int, input()))
        arr1.append(sol)

for i in range(n):
    for j in range(m):
        sol = list(map(int, input()))
        arr2.append(sol)

print(arr1 + arr2)