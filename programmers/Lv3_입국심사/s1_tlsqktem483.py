def solution(n, times):
    """
    :param n:
    :param times:
    :return: ans

    이분탐색 => O(log N)
    """
    ans = 0

    l = min(times)
    r = max(times) * n

    while l <= r:
        m = (l + r) // 2
        p = 0

        for t in times:
            p += m // t

            if p >= n:
                break

        if p >= n:
            ans = m
            r = m - 1
        elif p < n:
            l = m + 1

    return ans