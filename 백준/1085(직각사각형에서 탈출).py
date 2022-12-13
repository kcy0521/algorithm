x, y, w, h = map(int, input().split())
xi, yi = 0, 0
if x > w/2:
    xi = w - x
else:
    xi = x

if y > h/2:
    yi = h - y
else:
    yi = y

if xi > yi:
    print(yi)
else:
    print(xi)
