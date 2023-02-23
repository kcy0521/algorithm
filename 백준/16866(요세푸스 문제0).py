# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 n명의 사람이 모두 제거될 때까지 계속 된다. 
# 제거 되는 순서를 나타내는 것이다. 
n, k = map(int, input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)

# 3번째수 빼기 위해 사용
cnt = 0
sol = []
while True:
    # 종료 조건(하나 빼기전에 확인해야함)
    if not arr:
        break
    
    # 맨앞에서 부터 하나씩 빼기 
    x = arr.pop(0)
    cnt += 1
    
    if cnt == k:
        cnt = 0
        sol.append(x)
    else:
        arr.append(x) 

print('<', end='')
for i in sol:
    if i == sol[-1]:
        print(i,end='')
    else: 
        print(i,end=', ')

print('>', end='')
        

    
    

