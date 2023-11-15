import sys
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    x = list(map(int,sys.stdin.readline().split()))

    if len(x) == 2:
        stack.append(x[1])
    else:
        if x[0] == 2:
            if stack:
                print(stack[-1])
                stack.pop(-1)
            else:
                print(-1)
        elif x[0] == 3:
            print(len(stack))
        elif x[0] == 4:
            if stack:
                print(0)
            else:
                print(1)
        elif x[0] == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
