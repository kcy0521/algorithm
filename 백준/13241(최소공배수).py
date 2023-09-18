A, B = map(int,input().split())

ans = 1
start = min(A,B)
while True:
    sol = start * ans
    if sol % max(A,B) == 0:
        print(sol)
        break
    ans += 1