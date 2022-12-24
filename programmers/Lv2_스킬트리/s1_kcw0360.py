def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        idx = 0    # 스킬 트리 선행 조건 idx
        flag = True    # 불가능한 스킬 트리인 경우 False
        for sk in skill_tree:
            if sk in skill:    # 선생 스킬에 포함되는 경우
                if sk == skill[idx]:    # 선행 스킬 순서와 현재 스킬 순서가 맞는지 확인
                    idx += 1
                else:    # 조건이 만족하지 않는 스킬트리인 경우 False
                    flag = False
                    break
        if flag:    # 스킬 트리가 사용가능 하다면 answer +1
            answer += 1

    return answer