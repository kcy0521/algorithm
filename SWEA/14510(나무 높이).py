T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 나무 갯수
    tree = list(map(int,input().split())) # 각 나무들 리스트
    day = 0 # 시작일 결과값으로 출력할 변수

    Y = max(tree) # 나무 최대길이
    
    for i in range(N): # 성장시켜야할 나무 길이
        tree[i] = Y - tree[i]
    ########## 여기까지는 문제 없는거 같다. 

    
    # 성장시킬 나무 갯수 최소화 시키기
    idx = 0
    while idx < N:
        if day % 2 == 1:
            min = 1
        else:
            min = 2

        if tree[idx] != 0 and tree[idx]-min > 0:
            x = 1

            while idx + x < N:
                if tree[idx + x] >= min:
                    tree[idx + x] -= min
                    day += 1
                    break
                x += 1

        else:
            idx += 1

    print(tree)
    ## 오늘은 방향성 잡은것으로만 만족하고 그만하자 좆같누





