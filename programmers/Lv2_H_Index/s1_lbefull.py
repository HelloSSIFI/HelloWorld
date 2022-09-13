def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    l = 0
    r = citations[0]
    while l <= r:                                               # 이진탐색
        m = (l + r) // 2                                        # 중간값 m을 인용 횟수로 사용
        i = 0
        while i < len(citations) and citations[i] >= m:         # 인용 횟수가 m을 넘는 논문 수를 i
            i += 1
        if i >= m:                                              # i가 m 이상이면
            answer = max(answer, m)                             # 결과값 갱신
        if m <= i:                                              # m과 i값에 따라 범위를 조절
            l = m + 1
        else:
            r = m - 1
    return answer


# print(solution([3, 0, 6, 1, 5]))
