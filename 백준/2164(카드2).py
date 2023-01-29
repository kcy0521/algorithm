N = int(input())
# 큐에대한 개념으로 접근하면 시간이 너무 오래 걸림
x = 0
if N != 1:
    while 2**x < N:
        x += 1

    print(2*(N-(2**(x-1))))
else:
    print(1)