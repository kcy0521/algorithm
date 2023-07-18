N,M = map(int,input().split()) # n은 정답의 갯수, m은 tc수

basket = [0] * (N +1)
for i in range(M):
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        basket[i] = c
    
for i in range(1,N+1):
    print(basket[i],end=' ')


