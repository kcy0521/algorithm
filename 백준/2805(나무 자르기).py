n, m = map(int,input().split())
# n = 나무의 갯수
# m = 가져가야할 나무의 길이

arr = list(map(int, input().split()))

# x를 기준으로 설정 
# 만약 엑스 보다 길이가 낮다면 패스
# 한번에 구하는 건 불가능 함 그럼 몇단계를 거쳐야 될까?
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) //2
    sol = 0
    for i in arr:
        if i >= mid:
            sol += i - mid
    
    if sol >= m:
        start = mid + 1
    else:
        end = mid -1
print(end)







