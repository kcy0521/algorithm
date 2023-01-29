# 길이가 짧은 것 부터
# 길이가 같으면 사전 순으로
# 중복이 존재한다.!!
import sys
N = int(sys.stdin.readline())
arr=[]
for _ in range(N):
    arr.append(sys.stdin.readline().strip())
arr2 = set(arr)
arr = list(arr2)
arr.sort()
arr.sort(key= len)

for i in arr:
    print(i)