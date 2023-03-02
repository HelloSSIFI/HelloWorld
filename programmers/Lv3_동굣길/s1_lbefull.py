def solution(m, n, puddles):
    puddles = set(map(tuple, puddles))                                  # puddles의 좌표를 튜플로 셋에 저장
    dp = [[0] * (m + 1) for _ in range(n + 1)]                          # 문제의 좌표와 맞게 인덱스를 1부터 사용하기 위해 행, 열 크기를 1씩 늘려서 리스트 선언
    dp[1][1] = 1                                                        # 초기 집의 위치를 경우의 수 1로 초기화
    for r in range(1, n + 1):                                           # 오른쪽과 아래로만 이동하므로
        for c in range(1, m + 1):                                       # 2차원 리스트를 위에서 아래, 왼쪽에서 오른쪽으로 탐색하여 경우의 수를 찾음
            if (c, r) in puddles:                                       # 물에 잠긴 곳이면 continue
                continue
            dp[r][c] += (dp[r - 1][c] + dp[r][c - 1]) % 1000000007      # 아니라면 위에서 이동한 경우와 왼쪽에서 이동한 경우를 더해줌
    return dp[n][m]


# print(solution(4, 3, [[2, 2]]))
