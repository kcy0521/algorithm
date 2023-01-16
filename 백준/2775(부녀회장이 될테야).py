# a층의 b호에 살면 아래층(a-1)의 1호부터 b호까지 사람들의
# 수의합을 데려와 살아야한다. 
# 1층 3호 에는 6명이 산다 0층 1호 1명 / 0층 2호 2명/ 0층 3호 3명/ 1층 1호 6명 1층 2호 
# k층의 n호에는 몇명이 살고 있는가?


T = int(input())
for _ in range(T):
    layer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    new = [0]*14
    k = int(input()) # 층
    n = int(input()) # 호

    for i in range(k): # 층수 
        for j in range(n): # 호수2
            new[j] = sum(layer[0:j+1])          

        for p in range(n):
            layer[p] = new[p]
    
    print(new[n-1])