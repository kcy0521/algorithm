n = int(input())
x = 1
if n != 0:
    for i in range(1,n+1):
        x = x * i
    
    xx = str(x)[::-1]
    
    sol = 0
    k = 0
    while sol == 0:
        if int(xx[k]) != 0:
            sol = 1
            break
        k += 1
    
    print(k)

else:
    print(0)