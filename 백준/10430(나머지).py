A,B,C = map(int,input().split())

one = (A+B)%C
two = ((A%C) + (B%C))%C
three = (A*B)%C
four = ((A%C) * (B%C))%C

print(one)
print(two)
print(three)
print(four)