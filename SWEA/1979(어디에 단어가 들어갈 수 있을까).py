T = int(input())

for tc in range(1,T+1):
    sol = 0
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    # arr_x = arr // 이렇게하면 주소값이 같아지는 문제가 발생한다.
    arr_x = [row[:] for row in arr]
    arr_y = [row[:] for row in arr]
    
    #가로 확인방법
    for i in range(N):
        for j in range(N):
            if arr_x[i][j] == 1:
                for x in range(1,N-j):
                    if arr_x[i][j+x] == 1:
                        arr_x[i][j] += 1
                        arr_x[i][j+x] = 0
                    else:
                        break 
    
    # 세로 확인하는 방법
    for i in range(N):
        for j in range(N):
            if arr_y[j][i] == 1:
                for x in range(1,N-j):
                    if arr_y[j+x][i] == 1:
                        arr_y[j][i] += 1
                        arr_y[j+x][i] = 0
                    else:
                        break 
    for i in range(N):
        sol += arr_x[i].count(K)
        sol += arr_y[i].count(K)

    print(f"#{tc} {sol}") 