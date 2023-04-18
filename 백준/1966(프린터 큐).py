T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    
    # 인덱스 순서대로 정렬해 논 리스트
    idx = list(range(n))
    # 그 인덱스리스트를 타겟으로 설정
    idx[m] = 'target'

    # 인쇄된 순서
    order = 0 

    while True:
        # imp의 첫 번째 값 = 최대??
        if imp[0] == max(imp):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        # imp의 첫 번째 값 != 최대
        else:
            # 주어진 중요도위치 마지막으로 옮김
            imp.append(imp.pop(0))
            # 인덱스의 위치 마지막으로 옮김
            idx.append(idx.pop(0))