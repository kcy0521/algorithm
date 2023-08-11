T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())

    arr = list(map(int,input().split()))

    bbang = 0
    P = [0] * 11112

    for i in range(N):
        P[arr[i]] += 1
    
    for i in range(11112):
        if i!=0 and i % M == 0:
            bbang += K
        if P[i] != 0:
            bbang -= P[i]
            if bbang < 0:
                print(f'#{tc} Impossible')
                break
    
    else:
        print(f"#{tc} Possible")