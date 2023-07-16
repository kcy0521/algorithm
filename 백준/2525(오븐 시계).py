x,y = map(int, input().split())
a = int(input())

min = a + y
hour = x
if min > 59:
    hour += min // 60
    min = min % 60
    if hour > 23:
        hour -= 24 
print(hour,min)