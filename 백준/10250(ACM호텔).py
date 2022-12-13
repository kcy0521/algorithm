T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())
    # 호텔층수, 각층의 방수, 몇번째 손님
    # 손님에게 배정되어야 하는 방의 번호
    h = 0
    w = 1
    for i in range(N):
        h += 1
        if h > H:
            h = 1 # 층수 넘어가면 초기화 시킴
            w += 1
            if w > W:
                w = 1
    if w < 10:
        w = '0' + str(w)
    # 호수 출력하기
    print(str(h) + str(w))