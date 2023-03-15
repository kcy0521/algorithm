import sys
n, m = map(int, sys.stdin.readline().split()) 

arr = list(map(int, sys.stdin.readline().split())) 

sol = [0] * (n + 1)

for i in range(1, n+1):
    sol[i] = arr[i-1] + sol[i-1]

print(sol)

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    print(sol[b]-sol[a-1])
