a = int(input())
b = list(input())
b = b[::-1]
sol = 0
cnt = 0
# 무조건 3자리 수이다.
for i in b:
    bb = int(i)
    print(a * bb)
    sol += a * bb * (10 ** cnt)
    cnt += 1

print(sol)