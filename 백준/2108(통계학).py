n = int(input())
sol = []

for i in range(n):
    a = int(input())
    sol.append(a)

sol.sort() # 순서대로 정렬

# 산술 평균
print(round(sum(sol)/n)) # 이부분 실수 하지 말기 # 반올림을 적용 안했다. round 적용해야함.

# 중앙값
print(sol[(n-1)//2])

# 최빈값
p_arr = [0] * 4001
m_arr = [0] * 4001

for i in range(n):
    idx = sol[i]
    if idx > 0: # 양수
        p_arr[idx] += 1
    elif idx < 0: # 음수
        m_arr[-idx] += 1
    else: # 0일때
        p_arr[idx] += 1

p = max(p_arr)
m = max(m_arr)
sol2 = []
if p > m:
    for i in range(4001):
        if p_arr[i] == p:
            sol2.append(i)
elif p < m:
    for i in range(4001):
        if m_arr[i] == m:
            sol2.append(-i)
else:
    for i in range(4001):
        if p_arr[i] == p:
            sol2.append(i)
    for i in range(4001):
        if m_arr[i] == m:
            sol2.append(-i)

sol2.sort()
if len(sol2) == 1:
    print(sol2[0])
else:
    print(sol2[1])

# 범위
print(max(sol) - min(sol))

