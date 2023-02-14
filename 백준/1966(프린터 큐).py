n = int(input())

for _ in range(n):
    m, idx = map(int, input().split())
    # m은 몇번째로 출력될까?
    sol = [0] * 11
    arr = list(map(int, input().split()))

    # 출력되면 없게 만들고 cnt 늘릴까?
    