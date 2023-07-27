arr = [list(input()) for _ in range(5)]

max_len = [0,0,0,0,0] # 전체 길이
cnt = 0 # 현재길이


sol =''

for i in range(5):
    max_len[i] = len(arr[i])

n = max(max_len)

for i in range(n):
    for j in range(5):
        if cnt <= max_len[j]-1: # 길이 확인하기
            sol += arr[j][i]
    cnt += 1

print(sol)