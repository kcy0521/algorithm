N = int(input())

# 1,1 -> 1,2 -> 2,1 -> 2,2 -> 1,3 -> 1,4 -> 2,3 -> 3,2 -> 2,4

# 5 4 3 2 1  지하 몇층인지 구해야 한다. 

total = 1
stare = 1

while total < N:
    stare += 1 # 왜 층수부터 숫자 업하는지 생각해보기
    total = total + stare
    

# 층수가 홀수인지 짝수인지 구분해야함 그래야 어느 방향부터 시작인지 알 수 있음
# (5,1) -> 홀수일때 (x,y) x > y
# (1,4) -> 짝수일때 (x,y) x < y

sol = total - N # 이게 몇번째 인지 아는 방법임.
x,y = 0,0 # 그냥 설정해놓기 

if total > 1:
    if stare % 2 != 0: # 홀수일때
       x = 1
       y = stare
       
       for i in range(sol):
        x += 1
        y -= 1
    
    else: # 짝수 일때
        x = stare
        y = 1
        for i in range(sol):
            x -= 1
            y += 1
else:
    x ,y = 1,1

print(f'{x}/{y}')

