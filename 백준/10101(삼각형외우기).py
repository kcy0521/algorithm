tri = [int(input()) for _ in range(3)]

if sum(tri) != 180:
    print('Error')
elif min(tri) == 60:
    print('Equilateral')
elif (tri[0] == tri[1] and tri[0] != tri[2]) or (tri[0] != tri[1] and tri[1] == tri[2]) or (tri[0]== tri[2] and tri[0] != tri[1]):
    print('Isosceles')
else:
    print('Scalene')