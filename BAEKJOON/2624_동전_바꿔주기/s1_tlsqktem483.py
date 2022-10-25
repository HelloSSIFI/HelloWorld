"""
PyPy 통과, Python3 시간초과
"""
T = int(input())
k = int(input())
coin = []
dp = [0] * (T+1)
dp[0] = 1

for _ in range(k):
    c, n = map(int, input().split())
    coin.append([c, n])

for c_val, cnt in coin:
    for m in range(T, 0, -1):
        for c in range(1, cnt+1):
            if c_val*c > T:
                break
            if m - c_val*c >= 0:
                dp[m] += dp[m - c_val*c]
print(dp[T])