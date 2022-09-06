import sys
sys.setrecursionlimit(10000)


def solution(alp, cop, problems):
    answer = 10000
    n = len(problems)

    max_al, max_cl = max(problems, key=lambda x:x[0])[0], max(problems, key=lambda x:x[1])[1]

    dp = [[float('inf')]*181 for _ in range(181)]
    dp[alp][cop] = 0

    def dfs(a, c, t):
        nonlocal answer

        if a >= max_al and c >= max_cl:
            answer = min(t, answer)
            return

        if dp[a][c] < t:
            return

        dp[a][c] = t

        for i in range(n):
            now = problems[i]
            if a < now[0]:
                dfs(now[0], c, t + now[0]-a)
            if c < now[1]:
                dfs(a, now[1], t + now[1]-c)
            if a >= now[0] and c >= now[1]:
                dfs(a+now[2], c+now[3], t+now[4])


    dfs(alp, cop, 0)

    return answer

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))