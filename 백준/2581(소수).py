def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

M = int(input())
N = int(input())

sol = []
for i in range(M,N+1):
    if prime(i):
        sol.append(i)
    
if len(sol) == 0:
    print(-1)
else:
    print(sum(sol))
    print(sol[0])

