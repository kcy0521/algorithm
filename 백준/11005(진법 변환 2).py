N, B = map(int,input().split())

# N 을 B로 나눈다.
# 나머지가 몇이 나오는지 확인한다. 그걸 빈 리스트에 저장한다.
# 위의 과정을 반복한다.
# N 이 B보다 작으면 (종료 조건 = sol) 반복을 그만한다.

sol = True

num = []

while sol == True:
    if N < B:
        sol = False
        if N > 9:
            num.append(chr(N + 55))
        else:
            num.append(str(N))
        break

    X = N % B
    if X > 9:
        num.append(chr(X + 55))
    else:
        num.append(str(X))
    N = N // B
num = num[::-1]

print("".join(num))