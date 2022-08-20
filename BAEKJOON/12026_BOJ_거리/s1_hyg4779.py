n = int(input())
dist = ' '+input()

boj = {'B': 'O', 'O': 'J', 'J': 'B'}
dp = [float('inf')]*(n+1)
dp[1] = 0

for i in range(1, n):
    now = dist[i]
    for j in range(i+1, n+1):
        if dist[j] == boj[now]:
            dp[j] = min(dp[j], dp[i]+(j-i)**2)

print(-1 if dp[n] == float('inf') else dp[n])