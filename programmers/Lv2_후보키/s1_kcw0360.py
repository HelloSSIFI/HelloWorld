from itertools import combinations


def solution(relation):
    cols = len(relation[0])

    combs = []
    for i in range(1, cols+1):
        combs.extend(combinations(range(cols), i))

    candidates = []
    for comb in combs:
        temp = set()

        for row in relation:
            tmp = []

            for i in comb:
                tmp.append(row[i])
            temp.add(tuple(tmp))

        # 유일성 검사
        if len(temp) == len(relation):
            flag = True

            # 최소성 검사
            for candidate in candidates:
                if set(candidate).issubset(set(comb)):
                    flag = False
                    break

            # 두 조건을 모두 만족하는 경우 candidates 배열에 추가
            if flag:
                candidates.append(comb)

    return len(candidates)