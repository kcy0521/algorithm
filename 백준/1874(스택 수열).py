# push 연산은 + 로
# pop 연산은 - 로
# 불가능한 경우 NO를 출력한다

n = int(input())

arr = []
sol = []
# 가장 마지막수랑 이제 들어갈 놈이랑 비교한다. 마지막 수가 더크면 - 출력
for i in range(n):
    a = int(input())
    arr.append(a)

# 하나의 수열을 만들 수 있다 라고 하네요... 
