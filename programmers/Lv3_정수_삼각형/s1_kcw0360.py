def solution(triangle):
    dp = [[0]*i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]    # 첫번째 수는 바로 저장

    for i in range(1, len(triangle)):    # 삼각형 y좌표 (꼭대기 => 바닥)
        for j in range(len(triangle[i])):    # 삼각형 x좌표
            # 양 끝은 계속 더하기만 하고, 가운데 있는 수들은 앞서 나온 층의 같은 idx의 수, 바로 전의 수 중 큰 수에 값을 더해 dp에 저장
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[len(triangle) - 1])    # 마지막 라인에서 가장 큰 수 출력