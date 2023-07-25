T = 20

num = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5, 'D0':1.0, 'F':0.0}

cnt = 0 # 점수 총합
base = 0

for i in range(T):
    arr = list(input().split())
    if arr[2] =='P':
        pass
    else:
        x = float(arr[1]) * num[arr[2]]
        cnt += x
        base += float(arr[1])

print(round(cnt/base,6))