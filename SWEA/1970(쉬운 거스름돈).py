T = int(input())

for tc in range(1,T+1):
    
    N = int(input())
    arr = [0] * 8
    
    if N >= 50000:
        arr[0] = N // 50000
        N = N % 50000

    if N >= 10000:
        arr[1] = N // 10000
        N = N % 10000

    if N >= 5000:
        arr[2] = N // 5000
        N = N % 5000

    if N >= 1000:
        arr[3] = N // 1000
        N = N % 1000

    if N >= 500:
        arr[4] = N // 500
        N = N % 500

    if N >= 100:
        arr[5] = N // 100
        N = N % 100
    
    if N >= 50:
        arr[6] = N // 50
        N = N % 50

    if N >= 10:
        arr[7] = N // 10

    print(f'#{tc}')
    print(*arr)