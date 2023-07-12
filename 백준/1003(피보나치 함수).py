T = int(input())

arr = [int(input()) for i in range(T)]

n = max(arr)

dp = [{1,0}] * n

if n < 2:
    dp[0] = {1,0}
    dp[1] = {0,1}

print(dp[0] + dp[1])
    
    

