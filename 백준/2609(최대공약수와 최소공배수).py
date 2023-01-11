#각자 공약수 구하기
# 최대공약수 구하기
# 최소 공배수 구하기
def in_number(x): # 공약수 구하는 함수 정의 하기
    xx = []
    k = 1
    while k <= x:
        if x % k == 0 :
            xx.append(k)
        k += 1
    
    return xx
     
a, b = map(int, input().split())

aa = in_number(a)
bb = in_number(b)
c =[]
for i in range(len(aa)):
    if aa[i] in bb:
        c.append(aa[i])

print(max(c))
print((a // max(c)) * (b // max(c)) * max(c))
