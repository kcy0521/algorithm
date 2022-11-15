# 리스트 안의 숫자가 규칙적인지 아닌지 물어보는 문제
# 1부터 순서대로 올라가는 문제
num = list(map(int, input().split()))
a = 0
d = 0
for cnt in range(7):
    if num[cnt] < num[cnt+1]:
        a += 1
    elif num[cnt] > num[cnt+1]:
        d += 1
    elif a > 0 and d > 0:
        break

if a == 7:
    print('ascending')
elif d == 7:
    print('descending')
else:
    print('mixed')

