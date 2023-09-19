tri = list(map(int,input().split()))

tri.sort()
while True:
    if tri[0] + tri[1] > tri[2]:
        break
    else:
        tri[2] -= 1


print(sum(tri))    