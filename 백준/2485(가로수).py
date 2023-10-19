# 유클리드 호재법 사용하면 매우 쉽게 풀 수 있다. 
from math import gcd

N = int(input())

arr = [int(input()) for _ in range(N)]

sol = []
for i in range(N-1):
    sol.append(arr[i+1] - arr[i])

sol = list(set(sol)) # 중복제거

g = sol[0]
for i in range(1,len(sol)):
    g = gcd(g,sol[i])

print((arr[-1] - arr[0]) // g + 1 - len(arr))



######### 여기는 내가 구해본 방식 이렇게 풀면 시간 초가 나온다. 
# 공약수 어케 구하노 
# 소수를 구해 놓고 소수 구해놓고 
# 그거랑 전체가 나누어 지면 pass 하는 방식은 어떨까?
# a,b = arr[0],arr[-1]
# if arr[0] == 1:
#     a = 2
# nums = []
# for i in range(a,b+1):
#     c = 0
#     for j in range(2,i):
#         if i % j == 0:
#             c = 1
#     if c == 0:
#         nums.append(i)
# idx = 0
# win = 1 # 최대 공약수
# while idx < len(nums):
#     for i in sol:
#         if i % nums[idx] != 0:
#            idx += 1
#            break
#     else:
#         win = nums[idx]
#         break

# print((arr[-1] - arr[0]) // win + 1 - len(arr))