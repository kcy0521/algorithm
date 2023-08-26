# 회전의 유무도 확인해야함
# 방향도 확인해야함 
# N극 0 / S극 1
# 현재 위치도 알아야한다. 
# 문제가 너무 복잡하다. [태엽의 번호, 회전방향] 3 7 번 -> 시계방향으로 주어짐. 몇번째 기어인지 확인 만약 나보다 뒤에있는 기어면 
# 내가 돌린 방향기준 반대 방향으로 돌아간다 인덱스가 1차이가나면 1씩 차이가 난다. 
# 양쪽 방향 2군대를 확인해야함. 왼쪽 오른쪽 2개를 다 확인해야함. 
# 맞으면 다음것도 확인해야함. 최대 인덱스 3개 조건을 거는데 인덱스 값 범위 벗어나지 말아야함. 


T = int(input())

for tc in range(1, T+1):
    K = int(input())
    
    gear = [list(map(int,input().split())) for _ in range(4)]

    problem = [list(map(int,input().split())) for _ in range(K)]

    for i in range(K):
        a,b = problem[i][0] - 1 ,problem[i][1]

        # 첫 시계 돌리기
        if b == 1: # 시계
            gear[a].insert(0,gear[a].pop())
        else: # 반시계
            gear[a].append(gear[a].pop(0))

        # 인접한 시계가 돌아가는지 확인하기 
        for j in range(2):
            x = 1
            idx = 1

            if j == 0: # 왼쪽
                while 0<= a + idx <=3 :
                    if gear[a +idx]