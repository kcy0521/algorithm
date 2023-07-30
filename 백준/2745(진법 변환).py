N, B = input().split()

B = int(B)

N = N[::-1]
sol = 0

for i in range(len(N)):
    if N[i].isalpha():
        sol += (ord(N[i])-55) * (B ** i)
    else:
        num = int(N[i])
        sol += num * (B ** i)

print(sol)