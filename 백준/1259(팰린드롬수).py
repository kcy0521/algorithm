#펠린드롭이면 yes
# 아니면 no  마지막 줄에 0써진다.
sol = 1
while sol == 1 :
    a = input()
    if a =='0':
        break
    
    b = a[::-1]
    if a == b:
        print('yes')
    else:
        print('no')
