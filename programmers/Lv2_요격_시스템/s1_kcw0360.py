def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])    # 개구간(s,e)의 끝지점 e를 기준으로 정렬
    check_point = -1    # 요격 미사일 발사 지점 (초기화)

    for target in targets:
        if check_point <= target[0]:    # 요격 미사일 발사 지점이 개구간 s보다 작거나 같은 경우
            answer += 1    # 요격 미사일 추가
            check_point = target[1]    # 발사 지점 갱신

    return answer