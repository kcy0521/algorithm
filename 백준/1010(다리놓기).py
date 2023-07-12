def fac(num):
    cnt = 1
    if num > 0:
        for i in range(1,num+1):
            cnt *= i

    return cnt


T = int(input())

for i in range(T):
    n,m = map(int,input().split())
    x = fac(m) // (fac(n) * fac(m-n))
    print(x)
     
    
    