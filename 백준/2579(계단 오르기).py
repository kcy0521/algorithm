n = int(input())

arr = list(int(input()) for _ in range(n))
dp = [0] * (n)
# 1. 계단은 +1 or +2 뿐이다. 
# 2. 연속된 3개의 계단을 밟으면 안된다. 
# 3. 마지막 도착 계단은 반드시 밟아야 한다. 
# 총점수의 최댓값을 구해라. dp에 대한 개념을 확실히 이해 해야한다. dp에 대한개념 

if len(arr) <=2:
    print(sum(arr))
else: # 계단이 3개 이상일 경우
    dp[0] = arr[0] # 첫번째 계단 수동 계산
    dp[1] = arr[0] + arr[1] # 둘째 계단까지 수동 계산
    for i in range(2,n):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]) # 이게 핵심코드
    print(dp[-1])