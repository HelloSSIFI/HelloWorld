from itertools import combinations as comb


def solution(relation):
    n, m = len(relation), len(relation[0])

    # 모든 조합 만들기
    combs = []
    for i in range(1, m+1):
        combs.extend(comb(range(m), i))

    # 가능한 키 조합
    success = []
    for j in combs:
        tmp = [tuple([item[key] for key in j]) for item in relation]


        if len(set(tmp)) == n:


            for k in success:
                if set(j) >=set(k):
                    break
            else:
                success.append(j)

    return len(success)




print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))