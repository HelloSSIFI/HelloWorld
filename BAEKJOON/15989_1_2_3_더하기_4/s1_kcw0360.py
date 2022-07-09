import sys
input = sys.stdin.readline

T = int(input())

cases = [2, 3]
for i in range(T):
    number = int(input())
    dp = [1] * (number + 1)

    for case in cases:
        for i in range(case, number+1):
            dp[i] += dp[i-case]

    print(dp[number])


