from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = n*m+1

visit = [[0]*m for _ in range(n)]
visit[0][0] = 1
Q = deque([(0, 0, 1)])

while Q:
    nr, nc, cnt = Q.popleft()

    if nr == n-1 and nc == m-1:

        res = min(res, cnt)
        continue

    for d in direct:
        r, c = nr+d[0], nc+d[1]
        if 0 <= r < n and 0 <= c < m and not visit[r][c] and arr[r][c] == '1':
            visit[r][c] = 1
            Q.append((r, c, cnt+1))

print(res)