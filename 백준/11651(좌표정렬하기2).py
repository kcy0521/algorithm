N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([y,x])

# arr.sort()
xxx = sorted(arr)

for i in range(N):
    print(xxx[i][1],xxx[i][0])