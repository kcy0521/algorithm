n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

arr = coin[::-1]
cnt = 0
idx = 0 
hipe = 0

while k != hipe:
    
    if hipe + arr[idx] > k:
        idx += 1
    else:
        hipe += arr[idx]
        cnt += 1
    
print(cnt)
