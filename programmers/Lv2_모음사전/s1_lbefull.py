def solution(word):
    answer = 0
    cnt = 0
    order = ['A', 'E', 'I', 'O', 'U']


    def dfs(s):
        nonlocal answer, cnt
        if answer or len(s) > 5:                    # answer를 구했거나 길이가 5를 넘으면 리턴
            return

        if s == word:                               # word를 만들었으면
            answer = cnt                            # 순서를 기록
            return

        cnt += 1                                    # 단어가 바뀔때마다 cnt + 1
        for i in range(5):                          # AEIOU를 순서대로 붙여가면서 재귀
            dfs(s + order[i])


    dfs('')
    return answer


# print(solution('AAAAE'))
