a, b, v = map(int, input().split())
num = ((v-a) / (a-b))//1

if ((v-a) / (a-b)) -num > 0 :
    print(int(num + 2))
else:
    print(int(num + 1))

# while st < v:
#     # 낮 
#     st += a
#     if st >= v:
#         break
#     # 밤
#     st -= b
#     day += 1
# print(day)
# 이런식으로 하면 시간이 너무 오래걸린다.
