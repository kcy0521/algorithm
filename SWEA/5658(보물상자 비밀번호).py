T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())

    num = input()
    sol = []

    a = N // 4 # 한변의 수
    
    
    
    for i in range(a):
        if num[0:a] not in sol:
            sol.append(num[0:a])
        if num[a:2*a] not in sol:
            sol.append(num[a:2*a])
        if num[2*a:3*a] not in sol:
            sol.append(num[2*a:3*a])
        if num[3*a:4*a] not in sol:
            sol.append(num[3*a:4*a])
        
        num = num[N-1:N] + num[0:N-1]

    # 내림차순으로 나열하기!! 이것만 하면 될듯 
    sol.sort(reverse=True)  
    # 고른수 sol[K-1]을 숫자(10진법)로 바꾸기
    # int("0x1F7",16) -> 16진수를 10진수로 바꾸기
    nd = sol[K-1][::-1]
    r_sol = 0

    for i in range(a):
        if nd[i].isalpha() :
            r_sol += (ord(nd[i]) - 55) * (16**i)
        else:
            r_sol += int(nd[i]) * (16**i)


    print(f'#{tc} {r_sol}')