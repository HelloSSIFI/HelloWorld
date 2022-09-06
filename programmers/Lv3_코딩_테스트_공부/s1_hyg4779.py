def solution(alp, cop, problems):

    ma, mc = 0, 0
    for p in problems:
        ma = max(ma, p[0])
        mc = max(mc, p[1])

    dp = [[float('inf')]*(mc+1) for _ in range(ma+1)]
    alp, cop = min(alp, ma), min(cop, mc)
    dp[alp][cop] = 0

    for i in range(alp, ma+1):
        for j in range(cop, mc+1):

            if i + 1 <= ma:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)

            if j + 1 <= mc:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

            for a_req, c_req, a_rew, c_rew, cost in problems:
                if i >= a_req and j >= c_req:
                    next_a, next_c = min(ma, i+a_rew), min(mc, j+c_rew)
                    dp[next_a][next_c] = min(dp[next_a][next_c], dp[i][j]+cost)


    return dp[-1][-1]

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))