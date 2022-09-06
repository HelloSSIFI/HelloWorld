"""
1차 제출 : 4, 7, 8, 10 / 10 Fail (런타임 에러)
2차 제출 : alp, cop 값이 n_a, n_c 보다 큰 경우 대비 => AC
"""
def solution(alp, cop, problems):
    n_a, n_c = 0, 0
    for p in problems:
        n_a = max(n_a, p[0])
        n_c = max(n_c, p[1])

    dp = [[float('inf')] * (n_c + 1) for _ in range(n_a + 1)]
    alp, cop = min(alp, n_a), min(cop, n_c)
    dp[alp][cop] = 0

    for i in range(alp, n_a + 1):
        for j in range(cop, n_c + 1):

            # case 1
            if i + 1 <= n_a:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            # case 2
            if j + 1 <= n_c:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            # case 3
            for a_req, c_req, a_rew, c_rew, cost in problems:
                if i >= a_req and j >= c_req:
                    next_a, next_c = min(n_a, i+a_rew), min(n_c, j+c_rew)
                    dp[next_a][next_c] = min(dp[next_a][next_c], dp[i][j]+cost)

    return dp[-1][-1]


print(solution(10, 10,	[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))