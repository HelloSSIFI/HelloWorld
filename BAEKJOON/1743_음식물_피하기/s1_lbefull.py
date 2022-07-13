from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt = 1
            arr[i][j] = 2
            Q = deque()
            Q.append((i, j))
            
            while Q:                                # BFS 탐색
                r, c = Q.popleft()                  # 제일 많이 모여있는 음식물 수를 저장

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                        arr[nr][nc] = 2
                        cnt += 1
                        Q.append((nr, nc))

            result = max(result, cnt)

print(result)
