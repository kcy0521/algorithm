# 흰색, 검은색 8*8 크기 몇개의 정사각형을 다시 칠해야겠다고 생각
# 바꿔야되는 값의 최솟값을 구하면 된다.
m, n = map(int, input().split())

arr = [input() for _ in range(m)]

cnt = 0 # 모든 경우의 수 구하는거 가능
# 시작 위치 설정하기
for i in range(m-7):
    for j in range(n-7):
        
        if arr[j][i] == 'W':
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if l % 2 == 0 and k % 2 == 0 # 홀수가 b인지 알아보는 방법 짝수는 w로 확인해야함
        
        elif arr[j][i] == 'B':

