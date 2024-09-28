def solution(land):
    n = len(land)
    m = 4

    for i in range(1, n):
        for j in range(m):
            land[i][j] = land[i][j] + max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[n - 1])
