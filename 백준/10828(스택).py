def push(x):
    sol.append(x)

def Ans(x):
    

n = int(input())
sol = []
for i in range(n):
    arr = input().split()
    if len(arr) > 1:
        push(arr[1])
    else:
        if arr[0] == 'top':
            if sol:
                print(sol[-1])
            else:
                print(-1)
        elif arr[0] == 'size':
            print(len(sol))
        elif arr[0] == 'pop':
            if sol:
                print(sol.pop())
            else:
                print(-1)
        elif arr[0] == 'empty':
            if sol:
                print(0)
            else:
                print(1)

