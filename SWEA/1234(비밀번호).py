T = 10
for tc in range(1,T+1):
    N, M = input().split()
    N = int(N)
    A = list(M)
    
    while True:
        for i in range(N-1):
            if A[i] == A[i+1]:
                A.pop(i)
                A.pop(i)
                N -= 2
                break
        else:
            break
    sol = ''.join(s for s in A)
    print(f"#{tc} {sol}")