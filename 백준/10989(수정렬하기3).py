# N = int(input())
# arr = list(int(input()) for _ in range(N))
#
# for i in range(N-1):
#     idx = i
#     for j in range(i+1, N):
#         if arr[idx] > arr[j]:
#             arr[j], arr[idx] = arr[idx], arr[j]
#
# for i in range(N):
#     print(arr[i])
# 시간초과

import sys
N = int(sys.stdin.readline())
# 메모리가 초과된다고? 지랄하네 진자
arr = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)


