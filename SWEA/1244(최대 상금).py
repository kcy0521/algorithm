T = int(input())

for tc in range(1,T+1):
    N, M = input().split()
    M = int(M)

    nums = [int(N)]
    
    a = len(N)

    
    # 대가리가 ㅈㄴ 안돌아간다 
    cnt = 0
    for i in nums:
        X = list(nums[i])


    # 문제발생 첫번째 교환하고 두번째 교환할때 문제가 발생한다. 
    # 자리바꾸는 과정
        for i in range(a-1):
            for j in range(i,a):
                X[i],X[j] = X[j],X[i]
                if int(''.join(X)) not in nums:
                    nums.append(int(''.join(X)))
        cnt += 1
    
    sol = max(nums)
    
    print(nums)
    # print(f'#{tc}',sol)