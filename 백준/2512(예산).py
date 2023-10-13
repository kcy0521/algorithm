# 가능한 최대의 총 예산을 정한다
# 1.모든 요청이 배정될 수 있는 경우 요청한 금액을 그대로 배정한다

# 2. 모든 요청이 배정될 수 없는 경우에는 특수한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 
N = int(input())

checks = list(map(int,input().split()))

M = int(input())

if sum(checks) <= M:
    print(max(checks)) 
else:
    low,high = min(checks), max(checks)
    while True:
        mid = (low + high) // 2 # 평균값 
        sol = 0
        for i in checks:
            if i < mid:
                sol += i
            else:
                sol += mid

        if sol > 

