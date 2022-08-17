import sys
input = sys.stdin.readline


N = int(input())
street = list(input())
dp = [1000000] * N
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if street[j] == 'B' and street[i] == 'O':
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

        elif street[j] == 'O' and street[i] == 'J':
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

        elif street[j] == 'J' and street[i] == 'B':
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

if dp[N-1] == 1000000:
    print(-1)
else:
    print(dp[N-1])
