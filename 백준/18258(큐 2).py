import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])
for i in range(N):
    x = sys.stdin.readline().split()

    if x[0] == 'push':
        queue.append(x[1])
    elif x[0] == 'pop':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
