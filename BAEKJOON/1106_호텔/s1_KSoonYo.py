import sys
input = sys.stdin.readline

C, N = map(int, input().split())
dp = [0] * (1000 * 20 + 1)
costs = {}
for _ in range(N):
    cost, people = map(int, input().split())
    costs[cost] = people

last = 0
for c in range(1, len(dp)):
    possible = []
    for p in costs.keys():
        if p <= c:
            possible.append(p)

    for nc in possible:
        dp[c] = max(dp[c], dp[c - nc] + costs[nc])
    
    last = c
    if dp[c] >= C:
        break
print(last)
