import sys
# 원형으로 놓여 있다 원형이라고 생각하니까 어렵나? 흠... 
N = int(input())

circle = list(map(int,sys.stdin.readline().split()))
sol = [0] * N # 정답
check = [0] * N
idx = 0 # 현재위치

for i in range(N):
    x = circle[i]
    
