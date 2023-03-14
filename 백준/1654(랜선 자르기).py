k, n = map(int, input().split())

# 최대 랜선의 길이를 구하는 프로그램을 작성하시오. 

# 입력을 k개 받아야 한다. 
line = []
for i in range(k):
    line.append(int(input()))

# n 개로 만들어야하는데...
'''
a,b,c,d = 가지고 있는 선의 갯수
x = 구하고 싶은 길이
n = 만들어야 하는 갯수
aa + bb + cc + dd = n
n * x <= a + b + c + d
가장 길었을때는 d = x 일때 이다.
손실된 길이... 이걸 어떻게 표현 해야 할까?
'''