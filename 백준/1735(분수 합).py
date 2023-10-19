from math import gcd

a,b = map(int,input().split())
c,d = map(int,input().split())

# 최소 공배수 구해라
sol = min(b,d)

i = 1
while True:
    x = sol * i 
    if x % max(b,d) == 0:
        y = a * (x // b) + c * (x // d)
        pr = gcd(x,y)
        print(y//pr, x//pr)
        break
    else:
        i += 1

