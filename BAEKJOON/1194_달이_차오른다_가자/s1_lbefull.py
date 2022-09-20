from collections import deque


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
Q = deque()
visited = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] == '0':
            Q.append((r, c, 1, 1))
            visited[r][c] = 1

while Q:
    r, c, key, cnt = Q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '#' and ((visited[nr][nc] | key) > visited[nr][nc]):
            new_key = key
            if arr[nr][nc].islower():
                new_key |= 1 << (103 - ord(arr[nr][nc]))
            
            elif arr[nr][nc].isupper() and (key & 1 << 71 - ord(arr[nr][nc])) == 0:
                continue

            elif arr[nr][nc] == '1':
                print(cnt)
                exit()
            
            visited[nr][nc] = new_key
            Q.append((nr, nc, new_key, cnt + 1))

print(-1)
