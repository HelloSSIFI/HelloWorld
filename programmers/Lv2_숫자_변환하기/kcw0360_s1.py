def solution(x, y, n):
    dp = [9876543210] * (y+1)
    dp[x] = 0

    for idx in range(x, y+1):
        if dp[idx] == 9876543210:
            continue

        if idx + n <= y:
            dp[idx+n] = min(dp[idx+n], dp[idx]+1)
        if idx * 2 <= y:
            dp[idx*2] = min(dp[idx*2], dp[idx] + 1)

        if idx * 3 <= y:
            dp[idx*3] = min(dp[idx*3], dp[idx] + 1)

    if dp[y] == 9876543210:
        return -1
    else:
        return dp[y]