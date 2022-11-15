
    # 이문제 이해가 안된다. 시발 뭐야 진짜 ㅈ같네
    # 인풋이 들어오지 않으면 종료 된다. 라는 것을 잘 모르겠다.
try:
    while input:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()

# try와 except의 이용 방법을 아는가 모르는가를 물어보는 문제이다.
# 인풋이 들어오지 않으면 종료하는 그런 방법을 생각해주게 하는 ㅈ같은 문제이다.