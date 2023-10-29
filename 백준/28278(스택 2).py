N = int(input())

stack = []

for i in range(N):
    x = list(map(int,input().split()))
    if x[0] == 1:
        stack.append(x[1])
    elif x[0] == 2:
        if stack:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    elif x[0] == 3:
        print(len(stack))
    elif x[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif x[0] == 5:
        if stack:
            print(stack[0])
        else:
            print(-1)
    