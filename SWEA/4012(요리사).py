# N개의 식재료가 존재함
# 식재료를 각각 N/2 개씩 나누어 두개의요리를 한다
import itertools

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    num = list(range(1,N+1))
    
    nums = list(itertools.permutations(num,N//2))
    #최소값을 구해라 경우의 수를 모두 구해본다. 12/34 , 13/24, 14/23 총 경우의 수는 3가지가 나온다. 이것만 딱 골라낼수 있는 방법을 잘 모르겠다. 
    # 총 경우의 수 구하는 방법 
    # 2개씩 분류하는 방법... 4개씩 분류 방법 5개씩 분류 방법 이런거 알아야되는데
    # 이런식으로 할수 있는 방법이 뭐가 있을까? 12 34 // 13 24 // 14 23 이런식으로 나누는 방법이 뭐가 있을까? 3가지로 1234 를 2개로 나누는 경우의 수
    # 1234 1324 1423 이렇게 분류하는 방법을 파이썬으로 구현 어떻게 해야할까? 진짜 모르겠다 진짜 ㅈ같네 진짜 진짜 모르겠음 시발 ㅈ같네  
    # 방문 배열 개수만큼 탐색해서
    # 2개의 요리를 하려고 한다. 2개의 집단으로 나누는 방법 
    # N 이 8인 경우?? 씨이팔 4개 4개로 나눈다 그 다음엔? 4개를 2개로 나눈다. 1234 경우의 수가 너무 많자나 시이발 
    # 아니 문제 푸는게 왜이리 힘들어 시발 진짜 너무 힘들자나 짜증나게 
    # 2개로 나누고 그것들의 이분탐색 이진탐색 
    # 이분탐색 이진탐색 ? 이런것들을 for문을 이용해서 진행시켜야한다. 