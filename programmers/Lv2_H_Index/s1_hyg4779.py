def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    l = 0
    r = citations[0]

    while l <= r:
        m = (l+r)//2
        idx = 0

        while idx < len(citations) and citations[idx] >= m:
            idx += 1
        if idx >= m:
            answer = max(answer, m)
            l = m+1

        else:
            r = m-1

    return answer


print(solution([3, 0, 6, 1, 5]))