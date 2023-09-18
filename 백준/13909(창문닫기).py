N = int(input())
win = [0] * N


for i in range(1,N+1):
    ans = 1
    while True:
        sol = ans * i
        if sol <= N:
            if win[sol-1] == 0:
                 win[sol-1] = 1
            else :
                 win[sol-1] = 0
        else:
            break
        
        ans += 1

print(sum(win))