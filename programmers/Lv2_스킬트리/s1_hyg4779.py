def solution(skill, skill_trees):
    answer = 0

    n = len(skill)
    pre = {skill[i]: set(skill[:i]) for i in range(n)}

    for now in skill_trees:
        learn = set()
        for s in now:
            # 해당 기술을 이미 배웠거나
            # 선행 기술 목록을 다 배웠다면
            if s in learn or learn & pre.get(s, set()) == pre.get(s, set()):
                learn.add(s)
            else:
                break
        else:
            answer += 1
    return answer if answer else -1


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))