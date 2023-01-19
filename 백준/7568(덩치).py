n = int(input())
arr =[]
arr2 = []
num = [0]*n

for _ in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])

# 나 빼고 다른놈들하고 비교해야함 이거 어캐 하노
for i in range(n):
    k = 1
    for j in range(n):
        if arr[i] == arr[j]:
            continue
        else:
            # 나보다 클경우
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                k += 1
            else:
                continue
    num[i] = k

for i in range(n):
    print(num[i],end=' ')
        

             
    