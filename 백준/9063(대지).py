N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

max_x = max(X)
min_x = min(X)
max_y = max(Y)
min_y = min(Y)

ans = (max_x - min_x) * (max_y - min_y)
print(ans)