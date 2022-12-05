N = int(input())
z = 1
cnt = 0
while z < N:
    cnt += 1
    z = z + cnt * 6

print(cnt + 1)