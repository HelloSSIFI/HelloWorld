from itertools import combinations


def solution(relation):
    cols = len(relation[0])

    combs = []
    for i in range(1, cols+1):    # 후보키 모든 경우 만든 후 저장
        combs.extend(combinations(range(cols), i))

    candidates = []
    for comb in combs:    # 후보 키가 될 수 있는지 확인
        temp = set()    # 중복 제거

        for row in relation:    # relation에서 확인
            tmp = []    # 임시 저장

            for i in comb:    # 후보 키에 해당 하는 값들만 tmp에 임시저장
                tmp.append(row[i])
            temp.add(tuple(tmp))    # 튜플로 만든 후 temp에 저장

        if len(temp) == len(relation):    # 중복 확인
            flag = True

            for candidate in candidates:    # 최소성 확인
                if set(candidate).issubset(set(comb)):
                    flag = False
                    break

            if flag:    # 중복 검사, 최소성 검사를 통과한 후보 키만 저장
                candidates.append(comb)

    return len(candidates)