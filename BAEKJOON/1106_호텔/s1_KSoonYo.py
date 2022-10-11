import sys
input = sys.stdin.readline

C, N = map(int, input().split())
dp = [float('inf')] * 100001
dp[0] = 0
promotions = {}
for _ in range(N):
    cost, people = map(int, input().split())
    promotions[people] = min(promotions.get(people, 100), cost)

for p in range(1, len(dp)):
    possible = []
    for people in promotions.keys():
        if people <= p:
            possible.append(people)
    for np in possible:
        dp[p] = min(dp[p], dp[p - np] + promotions[np])


print(min(dp[C:]))
