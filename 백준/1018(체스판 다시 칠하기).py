# 흰색, 검은색 8*8 크기 몇개의 정사각형을 다시 칠해야겠다고 생각
# 바꿔야되는 값의 최솟값을 구하면 된다.
m, n = map(int, input().split())
arr = [input() for _ in range(m)]

cnt = 64 # 모든 경우의 수 구하는거 가능
# cnt2 = 0
# 시작 위치 설정하기
for i in range(m-7):
    for j in range(n-7):
        # 시작위치 설정하면 그것부터 64개 확인하기
        # 밑에부터 확인하면 됨
        # 바꾸는 거면 +1 숫자 올리기 
        cnt2 = 0 # 꼭지점 초기화되면 숫자 초기화

        if arr[i][j] == 'W':
        # 64개 확인
            for k in range(8):
                for l in range(8):
                    # 증가되는 숫자 취급
                    if k % 2 == 0 and l % 2 == 0 and arr[i+k][j+l]=='B':
                        cnt2 += 1
                    elif k % 2 == 0 and l % 2 == 1 and arr[i+k][j+l]=='W':
                        cnt2 += 1
                    elif k % 2 == 1 and l % 2 == 0 and arr[i+k][j+l]=='W':
                        cnt2 += 1
                    elif k % 2 == 1 and l % 2 == 1 and arr[i+k][j+l]=='B':
                        cnt2 += 1
        
        elif arr[i][j] == 'B':
            for k in range(8):
                for l in range(8):
                    if k % 2 == 0 and l % 2 == 0 and arr[i+k][j+l]=='W':
                        cnt2 += 1
                    elif k % 2 == 0 and l % 2 == 1 and arr[i+k][j+l]=='B':
                        cnt2 += 1
                    elif k % 2 == 1 and l % 2 == 0 and arr[i+k][j+l]=='B':
                        cnt2 += 1
                    elif k % 2 == 1 and l % 2 == 1 and arr[i+k][j+l]=='W':
                        cnt2 += 1

for i in range(m-7,0,-1):
    for j in range(n-7,0,-1):
        
        cnt2 = 0 # 꼭지점 초기화되면 숫자 초기화
        
        if arr[i][j] == 'W':
            for k in range(8):
                for l in range(8):
                    if k % 2 == 0 and l % 2 == 0 and arr[i-k][j-l]=='B':
                        cnt2 += 1
                    elif k % 2 == 0 and l % 2 == 1 and arr[i-k][j-l]=='W':
                        cnt2 += 1
                    elif k % 2 == 1 and l % 2 == 0 and arr[i-k][j-l]=='W':
                        cnt2 += 1
                    elif k % 2 == 1 and l % 2 == 1 and arr[i-k][j-l]=='B':
                        cnt2 += 1
        
        elif arr[i][j] == 'B':
                for k in range(8):
                    for l in range(8):
                        if k % 2 == 0 and l % 2 == 0 and arr[i-k][j-l]=='W':
                            cnt2 += 1
                        elif k % 2 == 0 and l % 2 == 1 and arr[i-k][j-l]=='B':
                            cnt2 += 1
                        elif k % 2 == 1 and l % 2 == 0 and arr[i-k][j-l]=='B':
                            cnt2 += 1
                        elif k % 2 == 1 and l % 2 == 1 and arr[i-k][j-l]=='W':
                            cnt2 += 1
        if cnt2 < cnt:
            cnt = cnt2 # 최솟값 변경

print(cnt)