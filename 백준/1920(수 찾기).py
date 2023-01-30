n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# b 안의 숫자가 a안에 있는지 확인하기
# 중복이 있는가?
# 이분 탐색을 하면 빠르게 찾을 수 있다. 
a.sort()
for num in b:
    la, ra = 0, n-1
    sol = False
    while la <= ra:
        mid = (la + ra) //2
        if num == a[mid]:
            sol = True
            print(1)
            break
        elif num > a[mid]:
            la = mid + 1
        else:
            ra = mid - 1
    
    if not sol:
        print(0)
