from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(M)]
visited = [[0] * N for _ in range(M)]
Q = deque()

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

white = 0
blue = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:               # 아직 병사를 확인하지 않았으면
            visited[i][j] = 1
            Q.append((i, j))
            cnt = 1

            while Q:                        # BFS 진행
                r, c = Q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and arr[r][c] == arr[nr][nc]:
                        visited[nr][nc] = 1
                        cnt += 1
                        Q.append((nr, nc))
            
            if arr[i][j] == 'W':            # 합산은 문제 조건대로 제곱해서 합산
                white += cnt ** 2
            else:
                blue += cnt ** 2

print(white, blue)
