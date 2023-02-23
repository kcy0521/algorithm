# 현재 큐의 중요도를 확인한다
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면 이 문서를 인쇄하지 않고 큐의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

# 어떠한 문서의 인쇄 순서를 말해줘라

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인쇄 할지 말지 검사한다
    while True:
        for i in range(1,len(arr)):
            # 인쇄 불가능한 상황
            if arr[0] > arr[i]:
                x = arr.pop(0)
                arr.append(x)
                break
        else:
            # 인쇄 가능하다.
            arr.pop(0)
            break
    
    

    
            


    