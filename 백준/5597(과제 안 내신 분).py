arr = [0] * 31

for i in range(28):
    x = int(input())
    arr[x] = 1

result = []
for i in range(1,31):
    if arr[i] == 0:
        result.append(i)

print(result[0])
print(result[1])
