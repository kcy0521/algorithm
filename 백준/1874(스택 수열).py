n = int(input())

arr = []  # 주어진 수열
for i in range(n):
    x = int(input())
    arr.append(x)

stack = []  # 스택 저장할거
op = []  # 스택 push, pop 뭔지 저장하는 장소 + or - 저장하는 곳
cnt = 1  # 현재 스택에 저장할 번호

sol = True
for i in arr:  # 4
    # 스택의 마지막 숫자가 같은지 아닌지 확인하면됨.
    # cnt = 8일때 while 탈출하는 방법..?
    # 중간에 탈출하는 방법은 무엇일까?
    while True:
        if stack:
            if stack[-1] != i:
                stack.append(cnt)
                op.append('+')
                if cnt <= n:
                    cnt += 1
                else:
                    sol = False
                    break
            else:
                stack.pop()
                op.append('-')
                break  # 이게 while문 break가능한가? for문 아니니깐 가능할거 같다. 가능이라 판별?
        else:
            stack.append(cnt)
            cnt += 1  # 아니면 이부분 근데 이부분은 문제가 안될거 같음 왜 와이 STACK이 비기가 힘듬.
            op.append('+')

if not sol:
    print('NO')
else:
    for i in op:
        print(i)
