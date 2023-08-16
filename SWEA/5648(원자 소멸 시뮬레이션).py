T = int(input())

for tc in range(1,T + 1):
    N = int(input())
    
    arr = [list(map(int,input().split())) for _ in range(N)]

    sol = 0
    
    for i in range(N-1):
        for j in range(i+1,N):
            [x1,y1,n1,k1] = arr[i]
            [x2,y2,n2,k2] = arr[j]
            
            if x1 == 'x':
                pass
            elif arr[i][2] == 0:
                if x1 > x2 and y1 < y2 and n2 == 3 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 == x2 and y1 < y2 and n2 == 1:
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 < x2 and y1 < y2 and n2 == 2 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
            
            elif arr[i][2] == 1:
                if x1 > x2 and y1 > y2 and n2 == 3 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 == x2 and y1 > y2 and n2 == 0:
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 < x2 and y1 > y2 and n2 == 2 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
            
            elif arr[i][2] == 2:
                if x1 > x2 and y1 > y2 and n2 == 0 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 > x2 and y1 == y2 and n2 == 3:
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 > x2 and y1 < y2 and n2 == 1 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
            
            elif arr[i][2] == 3:
                if x1 < x2 and y1 > y2 and n2 == 0 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 < x2 and y1 == y2 and n2 == 2:
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
                elif x1 < x2 and y1 < y2 and n2 == 1 and abs(x1-x2) == abs(y1-y2):
                    sol += (k1 + k2)
                    arr[i] = ['x','x','x','x']
                    arr[j] = ['x','x','x','x']
            # print(sol,i)
    print(f"#{tc} {sol}")