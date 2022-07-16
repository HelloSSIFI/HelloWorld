'''N = int(input())

dp = [n for n in range(N+1)]
M = 0
for i in range(4, N+1):
    tmp = dp[i]
    dp[i] = max(dp[i-3]+3, 2*dp[i-4], dp[i-1] + M if M else 0)
    M = dp[i] - tmp

print(dp)'''

N = int(input())
dp = [n for n in range(102)]

for i in range(6, 101):
    dp[i] = max(dp[i-3]*2, 3*dp[i-4], dp[i-5]*4)

print(dp[N])