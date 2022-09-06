def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0    # 모든 문제를 풀기 위한 alp, cop의 최대값
    for p in problems:
        max_alp = max(p[0], max_alp)
        max_cop = max(p[1], max_cop)

    # 모든 문제를 풀기 위한 alp, cop의 커트라인이 초기값으로 주어지는 값보다 낮을 수도 있다.
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    dp = [[9876543210]*(max_cop+1) for _ in range(max_alp+1)]    # dp[alp][cop]
    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)

            if j+1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

            for a, b, c, d, e in problems:    # 모든 문제 체크
                if i >= a and j >= b:    # 현재 alp, cop로 해당 문제를 풀 수 있을 경우
                    nxt_alp = min(max_alp, i+c)    # alp 최대치와 문제 풀고 얻은 alp 값과 비교
                    nxt_cop = min(max_cop, j+d)    # cop 최대치와 문제 풀고 얻은 cop 값과 비교
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j]+e)    # 해당 alp, cop 위치에 시간 누적

    return dp[-1][-1]