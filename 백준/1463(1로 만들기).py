# x가 3으로 나뉘면 3으로 나눈다. 
# 2로 나누어 지면 2로 나눈다)
# 둘다 안되면 1을 뺀다.
# 연산 몇번했는지 구해라

n = int(input())

cnt = 0
while n> 1:
    if n > 10:
        if n % 3 == 0:
            n = n //3 
            cnt += 1
        
        elif n % 2 == 0:
            n = n //2
            cnt += 1
        
        else:
            n = n - 1
            cnt += 1
    else:
        if n % 3 == 0 and n % 5 != 0:
            n = n //3 
            cnt += 1
        
        elif n % 2 == 0 and n % 5 != 0:
            n = n //2
            cnt += 1
        
        else:
            n = n - 1
            cnt += 1
        

print(cnt)

