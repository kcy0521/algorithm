T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    sol = 0 # 이득을 더하기 
    
    # 내림 인지 올림인지 확인할까?
    x = list(arr)
    x.sort()

    print(arr)
    print(x)