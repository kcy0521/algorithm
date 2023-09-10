def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

N = int(input())
sol = []
for i in range(1,N+1):
    if N % i == 0:
        sol.append(i)

sol_2 = []
for i in sol:
    if prime(i):
        sol_2.append(i)

sol_3 = []
for i in sol_2:
    cnt = 0
    nn = N
    while True:
        if nn % i == 0:
            cnt += 1
            nn = nn // i
        else:
            sol_3.append(cnt)
            break

for i in range(len(sol_3)):
    for _ in range(sol_3[i]):
        print(sol_2[i])