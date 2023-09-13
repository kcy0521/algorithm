N = list(input())
for i in N:
    i = int(i)

N.sort()
N = N[::-1]
print("".join(N))
