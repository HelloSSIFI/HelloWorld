from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)                                           # 선택한 직군을 key로 하여 몇번 지원자가 포함되는지 딕셔너리와 리스트로 표현
    info.sort(key=lambda x: int(x.split(' ')[-1]))                          # 이진 탐색을 할 예정이므로 info를 점수순서로 정렬
    sorted_score = list(map(lambda x: int(x.split(' ')[-1]), info))         # 점수만을 모아놓은 리스트
    for i in range(len(info)):
        informs = info[i].split(' ')[:-1]                                   # 점수를 제외하고
        for j in range(1, 5):                                               # 현재 지원자가 선택한 직군을
            for inform in combinations(informs, j):                         # 1~4까지 이름을 붙여 조합하여 해당하는 모든 key에 지원자의 인덱스를 넣음
                inform = ''.join(inform)
                info_dict[inform].append(i)
    info_dict[''] = list(range(len(info)))                                  # 빈 문자열에는 모든 지원자를 넣어줌

    for q in query:                                                         # 쿼리문 순회
        q = q.split(' ')                                                    # 빈 칸 기준으로 나눈 후
        group = []                                                          # 어느 그룹을 찾을건지 쿼리문을 붙여줌
        for i in range(0, len(q) - 1, 2):                                   # 이때 - 는 무시하고 문자열을 붙여줌
            if q[i] == '-':                                                 # 해당 그룹에 있는 지원자 리스트를 target으로 가져옴
                continue
            group.append(q[i])
        group = ''.join(group)

        target = info_dict[group]
        score = int(q[-1])                                                  # 기준 점수를 score로 저장
        l = 0                                                               # target 리스트를 이진탐색으로 탐색하면서
        r = len(target) - 1                                                 # 기준 점수보다 높은 가장 작은 인덱스를 찾아줌
        while l <= r:                                                       # target의 총 인원 수에서 인덱스를 빼준것이 최종 남는 인원
            m = (l + r) // 2
            if (sorted_score[target[m]] >= score):
                r = m - 1
            else:
                l = m + 1
        answer.append(len(target) - l)
    return answer


# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
