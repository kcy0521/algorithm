T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    # 5개이상!!! 6이여도 yes로 나와야한다. 
    # 8 개의 방향이 존재한다. 
    # try execpt 문을 사용하면 될것이다. 
    sol = 'NO'
    for i in range(N):
        if sol == 'YES':
            break
        
        for j in range(N):
            if sol == 'YES':
                break

            if arr[i][j] == 'o':
                
                for k in range(8): # 8번의 방향 
                    idx = 1
                    check = 1

                    if sol == 'YES':
                        break
                    
                    if k == 0: # 오른쪽 확인
                        while True:
                            try:
                                if arr[i][j+idx] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    else:
                                        idx = 1
                                        check = 1
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break
                    elif k == 1: # 왼쪽
                        while True:
                            try:
                                if arr[i][j-idx] == 'o':
                                    check += 1
                                    
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break
                    
                    elif k == 2: # 아래
                        while True:
                            try:
                                if arr[i+idx][j] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break
                    elif k == 3: # 위 
                        while True:
                            try:
                                if arr[i-idx][j] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break

                    elif k == 4: # 위 대각선 왼쪽
                        while True:
                            try:
                                if arr[i-idx][j-idx] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break
                    elif k == 5: # 위 대각선 오른쪽
                        while True:
                            try:
                                if arr[i-idx][j+idx] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break
                        
                    elif k == 6: # 아래 대각선 왼쪽
                        while True:
                            try:
                                if arr[i+idx][j-idx] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break
                    elif k == 7: # 아래 대각선 오른쪽
                        while True:
                            try:
                                if arr[i+idx][j+idx] == 'o':
                                    check += 1
                                else:
                                    if check >= 5:
                                        sol = 'YES'
                                    break
                                idx += 1
                            except:
                                if check >= 5:
                                    sol = 'YES'
                                break

    print(f"#{tc} {sol}")
