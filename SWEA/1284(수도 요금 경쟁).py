# 1리터당 p
# Q + 리터당 s

T = int(input())

for tc in range(1,T+1):
    P,Q,R,S,W = map(int,input().split()) 
    # A사
    A = P * W
    # B사
    if R >= W:
        B = Q
    else:
        B = (W - R) * S + Q

    sol = 0

    if A >= B:
        sol = B
    else:
        sol = A
    print(f"#{tc} {sol}")