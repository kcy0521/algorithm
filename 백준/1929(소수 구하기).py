def solv(x):
    for i in range(2,x):
        if x % i == 0 :
            return False
    return True

m, n = map(int, input().split())

sol = []
for i in range(2, 1000000):
    if solv(i) == True:
        sol.append(i)


for i in range(m, n+1):
    if i in sol:
        print(i)
