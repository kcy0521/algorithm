n = int(input())

sol = 0
while True:
    x = int(n ** 0.5)
    n -= x**2
    sol += 1
    print(x)
    if n == 0:
        break
print(sol)