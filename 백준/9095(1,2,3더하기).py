n = int(input())
# 1 2 3 의 합으로 나타내는 방법의 수를 구하는 프로그램을 만들어라
# 규칙을 찾아내는 것이 중요했던 문제 매우 중요??

for i in range(n):
   m = int(input())
   dp = [0] * (m+1)
   
   for i in range(1,m+1):
      if i == 1:
         dp[1] = 1
      elif i == 2:
         dp[2] = 2
      elif i == 3:
         dp[3] = 4
      else:
         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
      
   print(dp[m])
