def solution(alp, cop, problems):
    R = alp
    C = cop
    for i in range(len(problems)):                          # 알고력과 코딩력의 최대치를 구해줌
        R = max(problems[i][0], R)
        C = max(problems[i][1], C)
    
    dp = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R - alp + 1):                            # 우선 공부만으로 걸리는 시간을 dp에 저장
        for c in range(C - cop + 1):
            dp[alp + r][cop + c] = r + c

    for _ in range(2):                                      # 최신화된 값이 반영이 안되므로 2번 반복
        for aq, cq, aw, cw, cost in problems:               # 각각 문제를 하나씩 순회
            for r in range(max(aq, alp), R + 1):            # 초기 알고력과 초기 코딩력부터 최대치까지 2차원 반복
                for c in range(max(cq, cop), C + 1):        # 현재 문제를 풀었을 때 값이 저장된 값보다 작으면 교체해줌
                    nr = min(r + aw, R)                     # 문제를 풀었을 때 알고력 혹은 코딩력이 최대치(R, C)를 넘을 수 있으므로
                    nc = min(c + cw, C)                     # 최대값을 R, C를 넘지 않도록 설정
                    dp[nr][nc] = min(dp[nr][nc], dp[r][c] + cost)
    
    return dp[R][C]


# print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
