# 연속을 구분해 낼 수 있는가?
# 점수 합산해서 구해보기
# 받는 문자열이 연속되어 구분지어야 한다.
T = int(input())

for tc in range(T):
    result = 0
    num = 0
    ox = list(input())
    n = len(ox)
    for i in ox:
        if i == 'O':
            num += 1
            result += num
        else:
            num = 0
    print(result)

# 이거 문제가 for i in ox가 가장 중요한 부분이라고 생각한다.
# 어떤 리스트 안에 항목들의 값을 표현하는 for문이기 때문에 엄청 중요하게 쓰일것이라 생가한다
# 이게 좀 중요한것 같다.
# for i in [a,b]: => 리스트 안의 a가 뭔지 b가 뭔지 순서대로 진행하는 방법임 중요