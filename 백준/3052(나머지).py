z = []
for i in range(10):
    x = int(input())
    y = x % 42
    if y not in z:
        z.append(y)

print(len(z))