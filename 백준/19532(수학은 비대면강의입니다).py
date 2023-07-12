a,b,c,d,e,f = map(int,input().split())


if (a - b*d/e) != 0:
    x = (c- b*f/e) / (a - b*d/e)
    if b != 0:
        y = (c -a*x) / b
    else: 
        y = 0
else: 
    x = 0
    if b != 0:
        y = c / b
    else:
        y = 0



print(x,y)