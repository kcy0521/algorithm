import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))

sol = []

while q:
    idx, paper = q.popleft()
    sol.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, sol)))
# 문제를 푸는 것은 이해가 되는데 이걸 적재적소에 사용하는 방법을 잘 모르겠다. join 과 enumerate, deque, rotate,  이런것들을 잘 알아보자 
# 이런식으로 정답만을 가지고 오는 방식은 복습을 하지 않는한 내 것이 안된다. 좀더 공부를 더 해보자 시바 진짜 혼자서는 못풀겠다. ㅈ같네