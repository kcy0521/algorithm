n = 1000000
a = [True] * (n+1)
m = int(n**0.5)

for i in range(2,m+1):
    if a[i] == True:
        for j in range(i+i,n+1,i):
            a[j] = False


T = int(input())

for _ in range(T):
    x = int(input())
    
    cnt = 0
    # 이범위를 지정한 이유는 2개의 덧셈이기 때문에 그중 한개만 확인을 해도 전부 확인 이 가능한 상태이기 때문인가? 
    # 어떤 경우의 수도 전부 만족 가능한가? 이런 의문을 가지지만 되니깐 이렇게 범위를 지정해
    #  놨겠지 시버것 골드바흐 이게 맞어 염병 그럼 파티션을 구한다고 하면 그냥 여기에 곱하기 
    # 2만 하면 파티션의 갯수를 구하는 것과 동의어 라고 생각해도 되는 것이겠지? 
    for i in range(2,x//2+1): # 이범위 부분을 왜 x//2+1 로 설정했는지 이해가 안된다
        if a[i] and a[x-i]:
            cnt += 1
    print(cnt)