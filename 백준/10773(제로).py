# 잘못된 수를 부를 때마다 0을 외침.
# 0이면 가장 최근의 수를 지운다. 

n = int(input())
sol = []
for i in range(n):
    x = int(input())
    if x == 0:
        sol.pop()

    else:
        sol.append(x)

print(sum(sol))