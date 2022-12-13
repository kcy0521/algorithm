T = int(input())
arr = []
for _ in range(T):
    a, b = map(int, input().split())
    arr.append([a, b])

# 선택 정렬이용하기
arr.sort()
print(arr)
# for i in range(T-1):
#     for j in range(i+1, T):
#         if arr[i][0] > arr[j][0]:
#             arr[i], arr[j] = arr[j], arr[i]
#         elif arr[i][0] == arr[j][0]:
#             if sum(arr[i]) > sum(arr[j]):
#                 arr[i], arr[j] = arr[j], arr[i]

for i in range(T):
    print(arr[i][0], arr[i][1])

