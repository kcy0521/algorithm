num = list(int(input()) for _ in range(3))
x = 1
for i in range(3):
    x *= num[i]

x = str(x)

# count함수를 사용해야될것 같다.
for i in range(10):
    print(x.count(str(i)))
