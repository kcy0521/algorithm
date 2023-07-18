N,M = map(int,input().split())

arr = list(range(1,N+1))

for i in range(M):
    x,y = map(int,input().split())
    arr_1 = arr[:x-1]
    arr_2 = arr[x-1:y][::-1]
    arr_3 = arr[y:]
    arr = arr_1 + arr_2 + arr_3

print(*arr)