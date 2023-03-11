n, k = map(int, input().split())

def facto(n):
    num = 1
    while n > 0:
        num = n * num
        n -= 1
    
    return num

print(int(facto(n)/(facto(k)*facto(n-k))))