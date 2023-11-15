import sys
from collections import deque

N = int(input())

deck = deque([])
for _ in range(N):
    x = list(map(int,sys.stdin.readline().split()))

    if len(x) == 2:
        if x[0] == 1:
            deck.append(x[1])
        elif x[0] == 2:
            deck.appendleft(x[1])
    else:
        if x[0] == 3:
            if deck:
                print(deck[-1])
                deck.pop()
            else:
                print(-1)
        elif x[0] == 4:
            if deck:
                print(deck[0])
                deck.popleft()
            else:
                print(-1)
        elif x[0] == 5:
            print(len(deck))
        elif x[0] == 6:
            if deck:
                print(0)
            else:
                print(1)
        elif x[0] == 7:
            if deck:
                print(deck[-1])
            else:
                print(-1)
        elif x[0] == 8:
            if deck:
                print(deck[0])
            else:
                print(-1)
        