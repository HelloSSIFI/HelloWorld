def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n    #

    while start <= end:
        mid = (start + end) // 2
        check = 0

        for i in times:
            check += mid // i

        if check >= n:
            answer = mid
            end = mid - 1

        elif check < n:
            start = mid + 1

    return answer