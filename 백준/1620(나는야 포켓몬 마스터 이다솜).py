n, m = map(int, input().split())

book = []

for i in range(n):
    x = input()
    book.append(x)

for i in range(m):
    x = input()
    if x.isalpha():
        print((book.index(x) + 1))
    else:
        k = int(x) - 1
        print(book[k])
