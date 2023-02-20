# word = input().upper()
# word_list = list(set(word))

# cnt = []
# for i in word_list:
#   count = word.count
#   cnt.append(count(i))

# if cnt.count(max(cnt)) > 1:
#   print("?")

# else:
#   print(word_list[(cnt.index(max(cnt)))])

# m, n = map(int, input().split())
# arr = [input() for _ in range(m)]
# cnt = 64
# for i in range(m-7,0,-1):
#     for j in range(n-7,0,-1):
        
#         cnt2 = 0 # 꼭지점 초기화되면 숫자 초기화
        
#         if arr[i][j] == 'W':
#             for k in range(8):
#                 for l in range(8):
#                     if k % 2 == 0 and l % 2 == 0 and arr[i-k][j-l]=='B':
#                         cnt2 += 1
#                     elif k % 2 == 0 and l % 2 == 1 and arr[i-k][j-l]=='W':
#                         cnt2 += 1
#                     elif k % 2 == 1 and l % 2 == 0 and arr[i-k][j-l]=='W':
#                         cnt2 += 1
#                     elif k % 2 == 1 and l % 2 == 1 and arr[i-k][j-l]=='B':
#                         cnt2 += 1
        
#         elif arr[i][j] == 'B':
#                 for k in range(8):
#                     for l in range(8):
#                         if k % 2 == 0 and l % 2 == 0 and arr[i-k][j-l]=='W':
#                             cnt2 += 1
#                         elif k % 2 == 0 and l % 2 == 1 and arr[i-k][j-l]=='B':
#                             cnt2 += 1
#                         elif k % 2 == 1 and l % 2 == 0 and arr[i-k][j-l]=='B':
#                             cnt2 += 1
#                         elif k % 2 == 1 and l % 2 == 1 and arr[i-k][j-l]=='W':
#                             cnt2 += 1
#         if cnt2 < cnt:
#           cnt = cnt2

# print(cnt)
'''
1 2 3 4-> 0층
1 3 6 10-> 1층
1 4 10 20-> 2층
1 5 15 35-> 3층 
# '''
# a = [1,2,3,-1,-2,-3]
# # a.pop()

# print(a.pop())
# print(a)
# import sys

# T = int(sys.stdin.readline())
# for _ in range(T):
#     a,b = map(int,sys.stdin.readline().split())
#     print(a + b)

n, m = map(int, input().split())

print(abs(n-m))