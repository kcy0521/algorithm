T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))
    nums = list(range(0,n))
    sol = []
    for i in range(n):
        x = [arr[i], nums[i]]
        sol.append(x)
    
    print(sol)


    