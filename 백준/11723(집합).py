import sys

N = int(sys.stdin.readline())
S = set()

print('---')
for i in range(N):
    sol = sys.stdin.readline().strip().split()
    
    if len(sol) == 1: # all or empty
        if sol[0] == 'all':
            S = set([i for i in range(1,21)])
        else:
            S = set()
    else:
        cmd = sol[0]
        num = int(sol[1])
        if cmd == 'add':
            S.add(num)
        elif cmd == 'remove':
            S.discard(num)
        elif cmd == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)

'''
시간복잡도에 대한 개념이 있어야함
뭐가 문제니?? 입력값이 300만 까지 주어지기 때문에 시간오류가 많이 뜬다. 
pypy로 하면 안된다. 근데 python 으로 하면된다. 
'''