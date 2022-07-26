"""
아이디어 : 2차원 배열 dp 에 합산값 중첩 -> 최종 max 값 도출

"""
def solution(triangle):
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for floor in range(1, n):
        for i in range(len(triangle[floor-1])):
            dp[floor][i] = max(dp[floor][i], dp[floor-1][i] + triangle[floor][i])
            dp[floor][i+1] = max(dp[floor][i+1], dp[floor - 1][i] + triangle[floor][i+1])
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))