sol = 0
while sol == 0:
    triangle = list(map(int, input().split()))
    triangle.sort()
    if triangle[0] == 0:
        break

    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print('right')
    else:
        print('wrong')

