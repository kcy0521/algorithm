X = int(input())

T = int(input())
sum = 0

for i in range(T):
    a,b = map(int,input().split())
    c = a * b
    sum += c

if sum == X:
    print('Yes')
else:
    print('No')