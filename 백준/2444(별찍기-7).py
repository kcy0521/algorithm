N = int(input())

k = 2*N - 1

for i in range(1,N+1):
    x = (N-i)*' '
    y = (k-2*(N-i))*('*')
    print(f"{x}{y}")

for i in range(N-1,0,-1):
    x = (N-i)*' '
    y = (k-2*(N-i))*('*')
    print(f"{x}{y}")