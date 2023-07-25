N = int(input())

cnt = 0

for i in range(N):
    word = list(input())
    sol = []
    ans = 0
    if len(word) != 0:
        sol.append(word[0])
    
    if len(word) > 1:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                sol.append(word[i+1])

    for i in range(len(sol)-1):
        if sol.count(sol[i]) > 1:
            ans = 1
            break

    if ans == 0:
        cnt += 1

print(cnt)