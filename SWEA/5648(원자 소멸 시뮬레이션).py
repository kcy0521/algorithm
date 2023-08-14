T = int(input())

for tc in range(1,T + 1):
    N = int(input())
    
    arr = [list(map(int,input().split())) for _ in range(N)]

    all = [[0]* 1000 for _ in range(1000)] # 좌표계가 필요하나? 이부분도 문제인데... 
    
    # 하나하나 일일이 확인해봐야 하는가? 이것도 변수인데? 
    # 아니 이걸 어떻게 알아
    for i in range(N):
        for j in range(i,N):
            arr[i]
            # 첫번째거와 두번째거 확인가능한가? N의 수가 바뀌어도 되는가? 부딛힌다면 예외 처리는 어떤식으로 해야할까? 
            # 1. 이동방향을 먼저 확인한다. 같은 위치에 있는 점이 존재하는가? 중간지점이 존재하는가? 만나는 장소가 존재하냐? 
            # 2. 
            



