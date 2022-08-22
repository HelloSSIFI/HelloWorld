import sys
input = sys.stdin.readline

N = int(input())
c = input()

dp = [float('inf')]*N
c_dict = {
    'B': 0,
    'O': 1,
    'J': 2
}

dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if (c_dict[c[j]] + 1) % 3 == c_dict[c[i]]:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

print(dp[N-1] if dp[N-1] != float('inf') else -1)