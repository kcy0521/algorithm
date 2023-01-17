N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if nums[i] == 1:
        cnt += 1
    
    else:
        for j in range(2,nums[i]+1):
            if nums[i] != i and nums[i] % i == 0:
                cnt += 1

print(cnt)        
