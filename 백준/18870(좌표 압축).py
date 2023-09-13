import sys

N = int(input())

arr = list(map(int,sys.stdin.readline().split()))
A = sorted(list(set(arr)))

dic = {A[i] : i for i in range(len(A))}


for i in arr:
    print(dic[i], end=' ')
