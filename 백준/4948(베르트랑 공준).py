n= 123456 * 2  # n은 범위를 구하는 코드이다.
a = [True] * (n+1) # 집합이다. 
m = int(n ** 0.5) # 이게 중요하다. n의 제곱근을 반올림 하는게 중요

for i in range(2,m+1):
    if a[i] == True:
        for j in range(i+i,n+1,i):
            a[j] = False

arr = [i for i in range(2,n+1) if a[i] == True]
while True:
    x = int(input())
    cnt = 0

    if x == 0:
        break
    
    for i in arr:
        if x < i <= 2*x:
            cnt += 1
        elif i > 2*x:
            break

    print(cnt)