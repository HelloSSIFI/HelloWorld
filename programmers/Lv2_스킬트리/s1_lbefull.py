def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        idx = 0                                     # skill의 순서대로 탐색할 인덱스
        for c in tree:                              # 현재 스킬트리 탐색
            if c in skill:                          # skill에 등록된 순서 중 하나라면
                if c != skill[idx]: break           # 현재 순서와 맞는지 확인 후 다르다면 break
                idx += 1
        else: answer += 1                           # 순서가 모두 맞다면 answer+1
    return answer


# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
