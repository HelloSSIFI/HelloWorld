from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 2
    Q = deque([(0, 0)])

    while Q:                        # BFS 탐색
        r, c = Q.popleft()

        for d in range(4):          # 4방향 탐색
            nr = r + dr[d]          # 인덱스 범위 내에 있고 벽이 아니고 방문하지 않은 곳이면
            nc = c + dc[d]          # 현재 거리 +1을 visited에 저장하고 Q에 위치를 enQ

            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))

    return visited[-1][-1] - 1


# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
