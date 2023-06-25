n, m = map(int, input().split())

book = {}

for i in range(1,n+1):
    x = input()
    book[i] = x
    book[x] = i

for i in range(m):
    y = input()
    if y.isdigit():
        print(book[int(y)])
    else:
        print(book[y])

'''
딕셔너리를 만들어서 확인해야할놈이 문자인지 숫자인지 확인한 후에 그다음에 정답을 유추하는 문제
'''
