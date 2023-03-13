def solv(x):
    for i in range(2,x):
        if x % i == 0 :
            return False
    return True

m, n = map(int, input().split())

sol = [] # 소수 저장하는 리스트
for i in range(m,n):
    if solv(i) == True and i != 1:
        sol.append(i)

for num in sol:
    print(num)


