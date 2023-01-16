# 회원들의 나이가 증가하는 순으로 나이가 같으면 먼저 가입한 사람
# 가입한 순서대로 주어진다... 
# i를 가입한 순서라고 취급하면 되는디... 왜 안되는거여

N = int(input())
arr = []
for i in range(N):
    a, b = input().split()
    arr.append([int(a),i,b])
arr.sort()

for k in range(N):
    print(arr[k][0],arr[k][2])