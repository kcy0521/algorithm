def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if not n:
    print(0)
else:
    sol = []
    real_num = my_round(n * 0.15)

    for i in range(n):
        x = int(input())
        sol.append(x)

    sol.sort()
    if real_num != 0:
        sol = sol[real_num:(-real_num)]
    
    xx = my_round(sum(sol) / len(sol))
    print(xx)