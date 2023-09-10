N,K = map(int,input().split())

sol = []
for i in range(1,N+1):
    if N % i == 0:
        sol.append(i)

if K > len(sol):
    print(0)
else:
    print(sol[K-1])