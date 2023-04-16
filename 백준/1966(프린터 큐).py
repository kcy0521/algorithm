T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))

    arr2 = list(set(arr)).sort() # 중요도 리스트
    queue = []

    while True:
    # 주어진 방법에 대해서 생각해
    # 1. 현재 큐의 가장 앞에 있는 문서의 중요도를 확인한다.abs(2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이문서를 인쇄 하지 않고 가장 뒤에 배치)
    if arr[0] 
    
