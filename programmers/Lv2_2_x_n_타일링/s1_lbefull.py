def solution(n):
    dp = [0, 1, 2]          # 현재 크기의 경우의 수는 가로가 1작은 상태에서 1자 타일을 붙이는 경우와, 2작은 상태에서 = 모양으로 타일을 붙이는 경우의 합
    [dp.append((dp[-1] + dp[-2]) % 1000000007) for _ in range(n - 2)]
    return dp[n]


# # print(solution(5))
