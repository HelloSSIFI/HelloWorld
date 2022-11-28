for _ in range(int(input())):
    dp = [1] * 10

    for _ in range(int(input())-1):
        for num in range(10):
            dp[num] = sum(dp[num:])

    print(sum(dp))