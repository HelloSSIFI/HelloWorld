def dfs(cnt, idx):                          # cnt: 고른 글자 수, idx: new_word의 인덱스
    global result
    if cnt == K:                            # K개 골랐으면
        v = 0
        for s in unknown:                   # 모르는 글자셋이 있는 리스트를 순회
            if new_known >= s:              # 현재 고른 조합셋이 모르는 글자셋을 포함할 경우
                v += 1                      # 카운트
        result = max(result, v)             # 결과 갱신
        return
    
    for i in range(idx, len(new_word)):     # 아직 고르지 않았으면
        new_known.add(new_word[i])          # 새로운 글자셋에 현재 글자 추가 후
        dfs(cnt + 1, i + 1)                 # 재귀
        new_known.remove(new_word[i])       # 다시 제거


N, K = map(int, input().split())
known = set('antic')                    # 필수로 알아야 하는 글자
unknown = []                            # 주어진 단어 중 모르는 글자를 셋으로 인덱스에 맞게 저장
new_word = set()                        # 모르는 모든 글자를 셋으로 저장
init_known_cnt = 0                      # 필수 글자로 읽을 수 있는 단어 수

for i in range(N):                      # 단어 개수만큼 순회
    temp = set(input()) - known         # 단어 중 필수 글자를 제외한 나머지 글자를 셋으로 저장
    if temp:                            # 필수 글자 이외의 글자가 있다면
        new_word.update(temp)           # new_word에 갱신
        unknown.append(temp)            # unknown에 추가
    else:                               # 필수 글자만으로 단어를 읽을 수 있으면
        init_known_cnt += 1             # 카운트

new_word = list(new_word)               # 조합을 만들기 위해 리스트로 변환
new_known = set()                       # 조합을 만들 때 선택된 단어를 저장할 셋
result = 0

if len(known) + len(new_word) <= K:     # 만약 모든 글자를 합쳤을 때 K 보다 작으면
    result = N                          # 모든 단어를 읽을 수 있으므로 N이 정답

elif K >= 5:                            # 필수 글자가 5글자 이므로 K가 그 이상일 경우
    dfs(5, 0)                           # 조합을 찾아냄
    result += init_known_cnt            # result에 초기 읽을 수 있는 단어 수를 더해줌

else:                                   # K가 5 이하이면 하나도 못읽으므로 결과는 0
    result = 0

print(result)
