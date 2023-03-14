n, m = map(int, input().split())

A = {}
for _ in range(n):
    a,b = input().split()
    A[a] = b

for i in range(m):
    c = input()
    print(A[c])