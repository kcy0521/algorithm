T = int(input())
arr = [[0] * 100] * 100

sol = 0

for i in range(T):
    a,b = map(int,input().split())

    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j] = 1

for i in range(100):
    sol += sum(arr[i])

print(arr)