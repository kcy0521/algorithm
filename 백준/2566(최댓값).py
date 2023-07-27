arr = [list(map(int, input().split())) for _ in range(9)]

max_i = 0
max_j = 0
max_cnt = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_cnt:
            max_cnt = arr[i][j]
            max_i = i
            max_j = j

print(max_cnt)
print(max_i + 1,max_j + 1)