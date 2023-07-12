n = int(input())
m = int(input())

# 1부터 n까지 수가 있는데 

arr = []
for i in range(m):
    x,y = map(int,input().split())
    arr.append([x,y])

print(arr)
