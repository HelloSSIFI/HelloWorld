from collections import deque

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visit = [[0]*m for _ in range(n)]
ans = 0

for r in range(n):
    for c in range(m):
        if arr[r][c] and not visit[r][c]:
            Q = deque([(r, c)])
            cnt = 0
            visit[r][c] = 1

            while Q:
                nr, nc = Q.popleft()
                cnt += 1
                for d in direct:
                    sr, sc = nr+d[0], nc+d[1]
                    if 0 <= sr < n and 0 <= sc < m and not visit[sr][sc] and arr[sr][sc]:
                        visit[sr][sc] = 1
                        Q.append((sr, sc))
            ans = max(ans, cnt)

print(ans)