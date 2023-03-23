def solution(scores):
    answer = 1
    wh = scores[0]
    wh_score = sum(wh)
    scores.sort(key=lambda x: (-x[0], x[1]))    # 근무 태도 점수 내림차순으로 정렬하여 추후 동료 평가 점수로만 비교
    check = 0

    for score in scores:
        if wh_score >= sum(score):    # 완호의 점수보다 작은 경우 pass
            continue

        if wh[0] < score[0] and wh[1] < score[1]:    # 완호가 인센티브를 받지 못하는 경우
            return -1

        if check <= score[1]:    # score[1]의 값이 check 보다 작은 경우는 인센을 받지 못하는 경우
            check = score[1]
            answer += 1    # 석차 카운트

    return answer