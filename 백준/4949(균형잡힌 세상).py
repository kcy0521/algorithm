# 온점으로 끝난다도 이용해야 할것 같은데... 
# 갯수만 맞으면 되는게 아님 ) 나 ] 이게 먼저 나오면 안된다. 
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다. 이게 뭔말이냐 시발럼아

# chat gpt는 맞았다고 하는데 백준에서는 틀렸다고 하네요 이유를 모르겠어요.[.]
while True:
    arr = input()
    if arr == '.':
        break

    if arr[-1] == '.':
        sol = []
        for i in range(len(arr)-1):
            if arr[i] == '(' or arr[i] == '[':
                sol.append(arr[i])
            elif arr[i] == ')' and len(sol) != 0: 
                if sol[-1] == '(':
                    sol.pop()
                else:
                    print('no')
                    break
            elif arr[i] == ']' and len(sol) != 0:
                if sol[-1] == '[':
                    sol.pop()
                else:
                    print('no')
                    break    
    
        else:
            if len(sol) == 0:
                print('yes')
            else:
                print('no')
    else:
        print('no')

