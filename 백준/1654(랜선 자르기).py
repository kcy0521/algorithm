k, n = map(int, input().split())

arr = []
for i in range(k):
    x = int(input())
    arr.append(x)

start, end = 1, max(arr)

while start <= end:
    mid = (start + end)//2
    sol = 0
    for i in arr:
        sol += i // mid
    
    if sol >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
