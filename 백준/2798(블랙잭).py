# M을 크게 외침 N장의 카드중에서 "M을 넘지 않으면서" M에 최대한 가까운 카드 3장의 합을 구해 출력하시오. 
# 5개중 3개만 뽑는 방법... 
# M = sol 인경우 를 고려 안하게 될수도 있다 그리고 sol < M 이라는 조건도 만족해야함. 

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans = M #근접도
ans2 = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sol = arr[i] + arr[j] + arr[k]
            if M >= sol and M-sol < ans:
                ans = M - sol
                ans2 = sol
print(ans2)          
