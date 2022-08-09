import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    S = defaultdict(list)
    dp = [0] * (N+1)
    degree = [0] * (N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        S[X].append(Y)
        degree[Y] += 1
    W = int(input())

    queue = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            dp[i] = D[i]

    while queue:
        c = queue.popleft()
        for p in S[c]:
            degree[p] -= 1
            dp[p] = max(dp[p], dp[c] + D[p])
            if degree[p] == 0:
                queue.append(p)

    print(dp[W])