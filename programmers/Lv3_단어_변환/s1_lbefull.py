from collections import deque


def solution(begin, target, words):
    N = len(begin)
    answer = 0
    pos = {}
    words = set(words)

    if begin not in words:                          # begin이 words에 없다면 추가
        words.add(begin)

    for word1 in words:                             # words의 각 요소를 반복하면서
        pos[word1] = []                             # 현재 단어랑 1글자만 단어를 찾아서
        for word2 in words:                         # pos 딕셔너리의 value값에 추가
            if word1 == word2:
                continue

            cnt = 0
            for i in range(N):
                if word1[i] != word2[i]:
                    cnt += 1

            if cnt == 1:
                pos[word1].append(word2)

    Q = deque([[begin, 0]])                         # Q에는 단어와 변환 횟수를 넣어줌
    visited = {begin}                               # visited에는 변환 된 적 있는 단어들을 넣어줌
    while Q:                                        # BFS 탐색
        word, cnt = Q.popleft()
        if word == target:                          # target이 완성되면 변환 횟수를 answer에 저장하고 반복종료
            answer = cnt
            break

        for nw in pos[word]:                        # 현재 단어에서 변환할 수 있는 단어들을 탐색
            if nw not in visited:                   # 만약 아직 변환된 적 없는 단어라면
                visited.add(nw)                     # visited와 Q에 추가
                Q.append([nw, cnt + 1])

    return answer


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
