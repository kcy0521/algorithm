T = int(input())

for tc in range(1,T+1):
    N,B = map(int,input().split())

    S = list(map(int,input().split()))
    
    nums = [0]
    for i in range(N):
        for j in range(len(nums)):
            sol = S[i] + nums[j]

            nums.append(sol)


    print(f"#{tc}",min([x-B for x in nums if x-B >= 0]))