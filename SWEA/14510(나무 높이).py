T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 나무 갯수
    tree = list(map(int,input().split())) # 각 나무들 리스트
    day = 0 # 시작일 결과값으로 출력할 변수

    Y = max(tree) # 나무 최대길이
    
    for i in range(N): # 성장시켜야할 나무 길이
        tree[i] = Y - tree[i]
    
    # 물을 매일 주는게 가장 빠르다 규칙 홀수날 1 짝수날 2 총 3의 길이를 매일매일 주는게 가능하다
    for i in range(N):
        day += 2 * (tree[i] // 3) # 한개의 나무에 매일 물을 줄 수 있느지 체크 2일씩 물주면 3씩 자라난다. 
        tree[i] = tree[i] % 3 # 0 1 2 로 구분된다 

    # 0 1 2 로 구분된 리스트 매일 물을 주는 방법으로 최소화 시켜본다. 1과 2인 것들 갯수 구해서 없애보자 
    one = tree.count(1)
    two = tree.count(2)
    # 내가 확인한건 2가 더 많다. 경우의 수를 생각해보자
    # 1이 많을때 2가 많을때 1과 2가 숫자가 같을때 0 일때 (만약 0일때 날자가 안올라가게 해야한다.)
    if one == two:
        day += one # 0일때는 숫자를 안더하게 된다. 
    elif one > two: # 1개인나무가 더 많을때 
        day += two * 2
        day += 1 + ((one - two - 1) * 2) # 1인 나무의 갯수를 1 3 5 이런식으로 성장시켜야함 
    elif two > one:
        day += one * 2
        day += (two - one)  // 2 * 3
        day += (two -one) % 2 * 2
    # 1 1 1 이때 1일 후 0 1 1 (2일후) 0 1 1 (3이후) 0 0 1 (4일후) 001 (5일후) 000 날에 5일을 추가하면됨
    # 12 12 1이 3개 5일 추가 되면됨. 29일이된다.... 그런데 25일이 정답임. 4일이 초기 12에서 생긴거 같은데... 
    print(f"#{tc} {day}")


