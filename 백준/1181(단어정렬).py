# 길이가 짧은 것 부터
# 길이가 같으면 사전 순으로
# 중복이 존재한다.!!

N = int(input())

arr=[0] * 20000
for _ in range(N):
    x = input()
    y = len(x)
    if [y,x] not in arr:
        arr.append([y,x])

arr.sort()
for i in range(len(arr)):
    if arr[i][1] != 0:
        print(arr[i][1])
