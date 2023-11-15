N = int(input())
arr = list(map(int,input().split()))

way = []

sol = 'Nice'
cnt = 1

while cnt <= N:
    if arr:
        if arr[0] == cnt:
            cnt += 1
            arr.pop(0)
        elif way and way[-1] == cnt:
            cnt += 1
            way.pop()
        else:
            way.append(arr.pop(0))
    else:
        if way[-1] == cnt:
            cnt += 1
            way.pop()
        else:
            sol = 'Sad'
            break

print(sol)