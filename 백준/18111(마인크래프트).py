# 땅고르기 빠르게 해야한다.
n,m,b = map(int, input().split())

# 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력해라.
arr = [list(map(int, input().split())) for i in range(n)]

# 시간 그리고 높이를 구해라
# 제거 2초 , 추가 1초
# 시간을 우선으로 설정하고, 시간이 같다면 높이를 후순위로 고려
min_cnt = 256
max_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] <= min_cnt:
            min_cnt = arr[i][j]
        if arr[i][j] >= max_cnt:
            max_cnt = arr[i][j]

x = max_cnt - min_cnt
for _ in range(x):

    for i in range(n):
        for j in range(m):
            # 점심 나가서 먹을거 같어 ...
