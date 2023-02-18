def sayyes(arr):
    x = len(arr)
    sol_1 = []
    sol_2 = []
    for i in range(x):
        if arr[i] == '(':
            sol_1.append(arr[i])
        elif arr[i] == '[':
            sol_2.append(arr[i])
        elif arr[i] == ')':
            sol_1.pop()
        elif arr[i] == ']':
            sol_2.pop()

arr = list(input())
