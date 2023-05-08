# 땅고르기 빠르게 해야한다.
n,m,b = map(int, input().split())

# 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력해라.
arr = [list(map(int, input().split())) for i in range(n)]

# 시간 그리고 높이를 구해라
# 제거 2초 , 추가 1초
# 시간을 우선으로 설정하고, 시간이 같다면 높이를 후순위로 고려

block = []

for i in range(n):
    for j in range(m):
        block.append(arr[i][j])

# 시간과, 블록을 고려하자 0 ~ 256, 땅의 높이가 높은것을 출력해라

max_h = max(block)
min_h = min(block)
if min_h > 256:
    min_h = 256
    max_h = 256

height = 0
time = 100000000

for i in range(min_h,max_h+1): # 최소 값부터 최대값까지
    x,y = 0,0 # y는 시간 x는 블록
    # i 값이 평탄화 높이가 된다.
    for num in block:
        if (num -i) > 0 :
            y += 2*(num - i)
            x += (num-i) # 들어온 블록 갯수
        
        elif (num - i) < 0:
            y += -(num-i)
            x -= -(num-i) # 필요한 블록갯수

    # 최소 높이부터 했을때 시간이 같다면 높이를 갱신하면 높이 최고일때도 고려가능
    if (b+x) >= 0 and time >= y: # 시간, 박스 유무 확인
        if time == y:
            height = max(height, i) # 높이가 높은 값을 선택
        else:
            time = y
            height = i
    
print(time,height)

### 예제 케이스 내가 직접 만들어보기 

