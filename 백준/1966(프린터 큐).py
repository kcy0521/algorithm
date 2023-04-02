T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))
    
    arr2 = list(set(arr))
    sol = [0] * n
    cnt = 1
    
    for i in arr2:
        for j in range(n):
            if not sol[j] and i == arr[j]:
                sol[j] = cnt 
                cnt += 1

            if sol[m] != 0:
                print(sol)
                print(sol[m])
                break            
        
    # 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
    # 이문서를 인쇄하지 않고 큐의 가장 뒤에 재배치 한다.
    


'''
 중요도를 확인해야함 
 중요도가 높아야 먼저 인쇄가 된다.
 위의 식은 순서가 바뀌는게 안나타나게 된다. 시부레 이걸 어떻게 해야 하냐 ㅅㅂ
 좀 ㅈ같네 
 x = 1
어떤 중요도들이 있는지 확인해봐라
arr = sorted()
순서도 기록을 해 놔야 할거 같은데... 이거 어떻게 해야하냐? 
셔츠도 입어야 하는디 ㄲㅂ 이거 집에 옷이 없으니 
'''