def solution(alp, cop, problems):
    answer = 0
    solved = set()
    max_alp, max_cop = max([pro1[0] for pro1 in problems]), max([pro2[1] for pro2 in problems])
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]             # dp[알고력][코딩력]
    
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        # 알고력 1 상승
        if i + 1 <= max_alp:
            dp[i + 1][cop] = min(dp[i + 1][cop], dp[i][cop] + 1)
        for j in range(cop, max_cop + 1):

            # 코딩력 1 상승
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            # 문제를 푸는 경우
            for number in range(len(problems)):
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[number]
        
                # 현재 문제를 풀 수 있다면
                if i >= alp_req and j >= cop_req:
                    ni, nj = min(i + alp_rwd, max_alp), min(j + cop_rwd, max_cop)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)
                    if number not in solved:
                        solved.add(number)

    answer = dp[-1][-1]
    return answer


# 다익 스트라를 이용한 풀이
import heapq

def solution(alp, cop, problems):
    max_alp, max_cop = max(x[0] for x in problems), max(x[1] for x in problems)
    table = [[int(1e9) for _ in range(151)] for _ in range(151)]
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    h = [(0, alp, cop)]
    table[alp][cop] = 0
    while h:
        curr_cost, curr_alp, curr_cop = heapq.heappop(h)
        if curr_alp >= max_alp and curr_cop >= max_cop:
            return curr_cost
        if table[curr_alp][curr_cop] <= curr_cost:
            for r_alp, r_cop, a_alp, a_cop, n_cost in problems:
                n_alp, n_cop = min(150, curr_alp + a_alp), min(150, curr_cop + a_cop)
                if curr_alp >= r_alp and curr_cop >= r_cop and curr_cost + n_cost < table[n_alp][n_cop]:
                    table[n_alp][n_cop] = curr_cost + n_cost
                    heapq.heappush(h, (curr_cost + n_cost, n_alp, n_cop))
