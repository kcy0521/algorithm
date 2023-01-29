# 소수 찾기라.... 어캐 찾누 뭐 함수라도 있어??
def solv(x):
    for i in range(2,x):
        if x % i == 0 :
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in nums:

    if i != 1 and solv(i) == True:
        cnt += 1

print(cnt)