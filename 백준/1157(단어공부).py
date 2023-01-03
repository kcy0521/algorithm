# 대문자와 소문자 구분 안한다.
# 빈리스트 만들어서 거기에 담어
word = input().upper()
word_list = []
idx = 0
idx_list = [0] * 27
for i in range(len(word)):
    if word[i] not in word_list:
        #test
        # 그 문자열의 수만큼 횟수 늘려야함
        # 이정도만하면 문자열의 종류를 찾아라 정도만 해결됨
        word_list.append(word[i])
        idx_list[idx] += 1
        idx += 1
    elif word[i] in word_list:
        # 그 단어가 위치한 리스트의 인덱스를 알아내는 코드가 무엇이 있을까?
        x = 0
        y = 0
        while y < 27:
            if word[y] != word[i]:
                y += 1
            if word[y] == word[i]:
                x = y
                break
        idx_list[x] += 1

sol = max(idx_list)
cnt = 0
idx2 =[]
for i in range(27):
    if idx_list[i] == sol:
        cnt += 1
        idx2.append(i)

if cnt >= 2:
    print('?')
else:
    print(word_list[idx2[0]])


'''
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))]'''

'''
string = string.upper() => 전부 대문자로 바꾸기
string = string.lower() => 전부 소문자로 바꾸기
list.index(값) => 인덱스를 찾아주는 메소드이다.
list.count(문자열) => 문자열 안에서 찾고 싶은 문자의 개수를 찾을 수 있다. 
'''