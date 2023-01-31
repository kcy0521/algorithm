n = int(input())
a = list(map(int, input().split()))

m = int(input())
arr = list(map(int, input().split()))

# arr에 있는 수가 a안에 있는지 검색해라
dummy_plus = [0]*10000001
dummy_minus = [0]*10000001
dummy_zero = 0
# a.sort()
for num in a:
    if num >= 0:
        dummy_plus[num] += 1
    else:
        dummy_minus[abs(num)] += 1

sol = [0] * m
for i in range(m):
    if arr[i] >= 0:
        sol[i] = dummy_plus[arr[i]]
    else:
        sol[i] = dummy_minus[abs(arr[i])]
    
for x in sol:
    print(x, end=' ')