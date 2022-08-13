N = int(input())
word = [input() for _ in range(N)]
word.sort()                                                     # 입력받은 단어 오름차순 정렬

result = set()                                                  # 접두사X 집합을 저장할 예정
result.add(word[0])                                             # 우선 첫번째 단어를 넣어줌
for i in range(1, N):                                           # 두번째 단어부터 순회
    for j in range(min(len(word[i - 1]), len(word[i]))):        # 이전 단어와 비교하면서 둘 중 길이가 더 작은 단어만큼 순회
        if word[i - 1][j] != word[i][j]:                        # 단어의 한 글자라도 다를 경우
            result.add(word[i])                                 # 현재 단어를 접두사X 집합에 넣어준 뒤 break
            break
    else:                                                       # 단어가 다른 단어의 접두어일 경우
        result.remove(word[i - 1])                              # 이전 단어를 집합에서 빼주고
        result.add(word[i])                                     # 현재 단어를 집합에 넣어줌

print(len(result))
