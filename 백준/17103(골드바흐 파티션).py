n = 1000000
a = [True] * (n+1)
m = int(n**0.5)

for i in range(2,m+1):
    if a[i] == True:
        for j in range(i+i,n+1,i):
            a[j] = False


T = int(input())

for _ in range(T):
    x = int(input())
    
    cnt = 0
    for i in range(2,x//2+1): # 이범위 부분을 왜 x//2+1 로 설정했는지 이해가 안된다
        if a[i] and a[x-i]:
            cnt += 1
    print(cnt)