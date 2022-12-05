N = int(input())

a = 0
while N >= 0:
    if N % 5 == 0:
        a += N // 5
        print(a)
        break
    N -= 3
    a += 1
else: # 위의 while 문이 거짓일 경우 -1을 출력하게 하는 문장
    print(-1)