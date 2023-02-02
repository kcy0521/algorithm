n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

# 확인작업에서 시간을 많이 쓰고 있나??? 
sol = list(set(a) & set(b))
sol.sort()
print(len(sol))
for i in sol:
    print(i)


