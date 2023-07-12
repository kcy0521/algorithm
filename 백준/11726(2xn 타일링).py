n = int(input())

# 경우의 수 (가로로 해야할때 가로 1개 2개 3개 ... 이런식으로 해보는게 좋을듯)

x = n // 2
cnt = 1

if n > 1:
    for i in range(1,x):
 