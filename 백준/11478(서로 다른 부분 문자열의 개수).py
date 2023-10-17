S = input()

sol = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        sol.add(S[i:j+1])
print(len(sol))