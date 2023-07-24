N = int(input())

cnt = 0
for i in range(N):
    word = list(input())
    sol = []
    all = 0
    x = 0
    for i in range(len(word)):
        if word[x] != word[i]:
            if word[x] not in sol:
                sol.append(word[x])
                x = i
            else:
                all = 1
                break
        if word[-1] in sol and word[-2] != word[-1]:
            all = 1

    if all == 0 :
        cnt += 1
    print(all)

print(cnt)
            

        

