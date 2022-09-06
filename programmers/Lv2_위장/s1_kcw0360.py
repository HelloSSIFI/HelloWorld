from collections import defaultdict


def solution(clothes):
    answer = 1
    closet = defaultdict(list)    # 입력받은 옷을 종류별로 저장
    for a, b in clothes:
        closet[b].append(a)

    for key in closet:
        # 옷 가지수 + 안입을 때
        answer *= len(closet[key]) + 1

    return answer - 1    # 아무것도 안입는 경우 제외