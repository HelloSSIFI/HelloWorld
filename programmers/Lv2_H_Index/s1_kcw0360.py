def solution(citations):
    answer = 0
    citations.sort(reverse=True)    # 인용수가 많은 것이 먼저 오도록 정렬

    for idx in range(len(citations)):
        if idx+1 <= citations[idx]:
            answer = idx + 1

    return answer