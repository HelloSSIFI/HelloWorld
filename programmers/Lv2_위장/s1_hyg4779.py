def solution(clothes):

    answer = 1

    hash_map = {}
    # 종류 별 몇벌이 있는지 더한다
    for prod, kind in clothes:
        hash_map[kind] = hash_map.get(kind, 0)+1

    # 해당 옷을 입는 모든 경우를 곱한다(+1 하는건 안입는 경우)
    for kind in hash_map:
        answer *= (hash_map[kind]+1)

    # 전체를 안 입는 경우를 뺸다
    return answer-1