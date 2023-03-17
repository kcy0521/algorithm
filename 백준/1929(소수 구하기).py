min_num, max_num = map(int,input().split())
a = [True] * (max_num+1)
x = int(max_num ** 0.5)

for i in range(2,x+1):
    if a[i] == True:
        for j in range(i+i,max_num+1,i):
            a[j] = False

for i in range(min_num,max_num+1):
    if a[i] == True and i >=2:
        print(i)
