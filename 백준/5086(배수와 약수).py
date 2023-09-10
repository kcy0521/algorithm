while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break

    sol_y = []
    

    for i in range(1,y+1):
        if y % i == 0:
            sol_y.append(i)
    
    if x in sol_y:
        print("factor")
    elif x % y == 0:
        print("multiple") 
    else:
        print("neither")
