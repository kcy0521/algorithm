N = int(input())
window = [0] * N

# 와 그냥 이전에 풀었던 방식 그대로 똑같이 풀었네 변수명만 다르고 그대로 똑같음... 
# 메모리 초과가 무슨뜻인가? 
# 너무많은 변수들을 배열등에 저장할 경우 다. 

# 좀더 빠르게 해결할 수 있는 방법은 무엇일까? 


# for i in range(1,N+1):
#     x = 1
#     while True:
#         a = (i * x) - 1 # 창문의 위치
#         if a > N - 1:
#             break

#         if window[a] == 0:
#             window[a] = 1
#         else:
#             window[a] = 0
#         x += 1

# print(sum(window))
# print(window)
result = 0
x = 1
while x*x <= N:
    x += 1
    result += 1
print(result)