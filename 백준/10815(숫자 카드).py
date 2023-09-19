M = int(input())
arr = list(map(int,input().split()))
N = int(input())
arr_2 = list(map(int,input().split()))

ans = []
for i in range(N):
    if arr_2[i] in arr:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)