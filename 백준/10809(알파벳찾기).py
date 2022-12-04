# 처음 등장 위치를 나타내라
S = list(input())

# check2 = ['a', 'b', ' c', 'd', 'e', 'f', 'g',
#           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
check = 'abcdefghijklmnopqrstuvwxyz'

for i in check:
    if i == 'z':
        if i in S:
            print(S.index(i))
        else:
            print(-1)
    elif i in S:
        print(S.index(i), end=' ')
        # 몇번째에 처음 등장하는지 알려주는 거임
    else:
        print(-1, end=' ')

# 인풋받는 단어를 리스트로 묶어주고 check를 저렇게 문자로 표현해야하는 이유를 잘 몰겠다
# 이부분 때문에 틀린횟수가 엄청 늘어났다. check2처럼 리스트로 표현하면 안되는 이유를 잘 모르겠다.
