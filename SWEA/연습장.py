# 기어를 돌린다 를 어떻게 구현할까? 
N = [1,2,3,4]

# 반시계 방향으로 돌림
N.append(N.pop(0))

# 시계 방향으로 돌림
N.insert(0,N.pop())

print(N)