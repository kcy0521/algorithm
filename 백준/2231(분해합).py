# m의 분해합이 n인 경우 m을 n의 생성자라고 한다. 
# 245의 분해합은 256(분해합) n = 245(생성자) m + 2 + 5 + 6
# 가장 작은 생성자를 구하는 프로그램을 작성하시오. 
# 100a + 10b + c + a + b + c


# 생성자가 없는경우
# 1,2,3,4,5,6,7,8,9,10, 11 = 10 + 1 + 0 12 = 11 + 1 + 1
n = int(input())
k = 1

while True:
    k += 1
    x = str(k)
    cnt = 0
    for i in range(len(x)):
        cnt += int(x[i])

    sol = cnt + k
    if k >= n:
        print(0)
        break

    if sol == n:
        print(k)
        break

