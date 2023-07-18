N,M = map(int,input().split())

arr = list(range(1,N+1))

for i in range(M):
    x,y = map(int,input().split())
    arr[x-1],arr[y-1] = arr[y-1],arr[x-1]

print(*arr)