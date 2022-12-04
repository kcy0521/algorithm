num = list(input().split())
a = num[0][::-1]
b = "".join(reversed(num[1]))

if a > b:
    print(a)
else:
    print(b)
