def solution(x, y, n):
    dp = [9876543210] * (y+1)    # dp 테이블(최소 카운트 누적)
    dp[x] = 0    # x는 카운트 0

    for idx in range(x, y+1):    # x값 이후 부터 체크
        if dp[idx] == 9876543210:    # 값이 만들어지지 않는 부분은 pass
            continue

        # idx가 y 보다 커지지 않도록 체크 & 문제에서 주어진 케이스 마다 카운트 체크
        if idx + n <= y:
            dp[idx+n] = min(dp[idx+n], dp[idx]+1)

        if idx * 2 <= y:
            dp[idx*2] = min(dp[idx*2], dp[idx] + 1)

        if idx * 3 <= y:
            dp[idx*3] = min(dp[idx*3], dp[idx] + 1)

    if dp[y] == 9876543210:    # y가 불가능한 경우 -1 리턴
        return -1
    else:
        return dp[y]