n, m = map(int,input().split())
# n = 나무의 갯수
# m = 가져가야할 나무의 길이

arr = list(map(int, input().split()))

# x를 구하는 문제 
# 둘째 줄에서 나무의 높이의 합은 항상 m보다 크거나 같다. 상근이는 집에 필요한 나무를 
# 항상 가지고 갈 수 있다.

x = min(arr)
cnt = 0