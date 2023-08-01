T = int(input())

for tc in range(1,T+1):
    # 1000명
    x = int(input())
    score = [0] * 101
    num = list(map(int,input().split()))
    for i in range(len(num)):
        score[num[i]] += 1

    max_score = 0
    N = max(score)
    # N이 2개일 경우를 고려 안함..
    for i in range(101):
        if N == score[i]:
            max_score = i

    
    print(f"#{tc} {max_score}")