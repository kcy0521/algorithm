N = int(input())
arr1 = list(map(int,input().split())) #상근이 꺼

M = int(input())
arr2 = list(map(int,input().split()))

# 딕셔너리 사용하는 방법
# _dict = {}
# for i in range(N):
#     _dict[arr1[i]] = 0

# for j in range(M):
#     if arr2[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')

# 이진탐색을 사용하는 방법


# 이진탐색을 하려면 해야 할 것 

# arr2 안에 있는 숫자가 arr1에 있는지 탐색해야한다. 
arr1.sort()

for check in arr2:
    low, high = 0,N-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if arr1[mid] > check:
            high = mid -1
        elif arr1[mid] < check:
            low = mid + 1
        else:
            exist = True
            break
    
    print(1 if exist else 0, end=' ')