# 동전의 갯수 최소화 하기
T = int(input())

for tc in range(T):
    N = int(input())

    Quarter = N // 25
    N = N % 25
    
    Dime = N // 10
    N = N % 10

    Nickel = N // 5
    N = N % 5

    Penny = N

    print(Quarter,Dime,Nickel,Penny)