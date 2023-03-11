# 알파벳이면 넘어가기
# 괄호면 저장하기
# 괄호가 맞지 않으면 바로 아웃( 조건 달기)

# 그전 상태가 2가 제거되면 그전이 1인지 2인지 알 수 없어진다. 

while True:
    arr = input()
    if arr == '.':
        break

    arr2 = arr.replace(" ", "")
    c1 = []

    for i in arr2:
        if i == '(':
            c1.append(i)
        
        elif i == '[':
            c1.append(i)
        
        elif i == ')' :
            if c1 and c1[-1] == '(':
                c1.pop(-1)
            else:
                print('no')
                break
        
        elif i == ']':
            if c1 and c1[-1] == '[':
                c1.pop(-1)
            else:
                print('no')
                break
        
    else:
        if c1:
            print('no')
        else:
            print('yes')



        

        
    
