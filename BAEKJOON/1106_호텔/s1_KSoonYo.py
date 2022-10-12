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

## 풀이 수정 후 통과 코드
import sys
input = sys.stdin.readline

C, N = map(int, input().split())
dp = [0] * (1000 * 1000 + 1)                # dp 최대 범위를 늘려줌
costs = {}
for _ in range(N):
    cost, people = map(int, input().split())
    costs[cost] = max(costs.get(cost, 0), people)

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



### best solution(by 재만님)
C, N = map(int, input().split())
dp = [0] + [100001] * C
for _ in range(N):
    cost, guest = map(int, input().split())         # 사람이 홍보해서 늘어나는 최소 고객보다 작으면 dp에 저장된 값과 cost 중 작은 값 선택
    for i in range(1, C + 1):                       # 최소 고객보다 많으면, 현재 i명에서 최소고객을 뺀 비용에 cost를 더한 값과 dp에 저장된 값 중 작은 값을 선택
        dp[i] = min(dp[i], cost) if i < guest else min(dp[i], dp[i - guest] + cost)
print(dp[C])
