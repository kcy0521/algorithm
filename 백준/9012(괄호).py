# vps인지 아니지 판단해서 결과를 말하라
n= int(input())
for _ in range(n):
    arr = input()
    sol = []
    if arr[0] =='(':
        sol.append(arr.pop(0))
    elif arr[0] == ')':
        sol.pop(-1)
    
    if len(sol) > 0 :
        print('No')
    else:
        print('YES')
    
