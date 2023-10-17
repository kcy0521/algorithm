N, M = map(int,input().split())

S = set(input() for _ in range(N))

sol = 0
for _ in range(M):
    x = input()
    if x in S:
        sol += 1

print(sol)