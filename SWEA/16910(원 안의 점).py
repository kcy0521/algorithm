T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 반지름

    cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if (i**2) + (j**2) <= N**2:
                cnt += 1
    sol = (cnt - N - 1) * 4 + 1
    print(f"#{tc} {sol}")

