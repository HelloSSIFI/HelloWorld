def solution(word):
    answer = 0
    cnt = 0    # 탐색 카운트
    words = ["A", "E", 'I', 'O', 'U']

    def dfs(tmp):    # 완전탐색
        nonlocal answer, cnt

        if tmp == word:    # 원하는 단어가 나오면 해당 탐색 순서를 answer에 저장
            answer = cnt
            return

        if len(tmp) == 5:    # word의 길이는 최대 5
            return

        for i in words:
            cnt += 1
            dfs(tmp + i)    # 재귀

    dfs('')

    return answer