from collections import deque


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
ate = 0
shark_r = 0
shark_c = 0
for r in range(N):
    for c in range(N):                                  # 상어를 공간에서 지워주고 좌표만 저장
        if arr[r][c] == 9:
            arr[r][c] = 0
            shark_r = r
            shark_c = c

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
shortest = 0
answer = 0
while shortest < 401:                                   # 다음 먹이가 없을 때까지 반복
    visited = [[0] * N for _ in range(N)]
    visited[shark_r][shark_c] = 1
    Q = deque()
    Q.append((shark_r, shark_c, 0))
    shortest = 401                                      # 거리가 가장 가까운 먹을 수 있는 물고기의 거리를 저장
    sr = 20                                             # 먹을 수 있고 가까운 물고기의 가장 위 가장 왼쪽 좌표를 저장
    sc = 20
    while Q and Q[0][2] < shortest:                     # BFS 탐색
        r, c, cnt = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= shark_size:
                visited[nr][nc] = 1
                Q.append((nr, nc, cnt + 1))
                if 0 < arr[nr][nc] < shark_size:        # 먹을 수 있는 물고기를 발견하면
                    shortest = cnt + 1                  # 거리를 갱신, BFS 탐색이므로 최단 거리가 저장됨
                    if nr < sr:                         # 최단 거리에 여러마리 일 경우 가장 위, 가장 왼쪽 좌표를 저장
                        sr = nr
                        sc = nc
                    elif nr == sr and nc < sc:
                        sc = nc

    if shortest < 401:                                  # 먹을 수 있는 물고기가 있다면
        ate += 1                                        # 먹은 물고기 수 + 1
        if ate == shark_size:                           # 현재 사이즈만큼 먹었다면
            shark_size += 1                             # 사이즈를 키워주고 먹은 수를 0으로 초기화
            ate = 0
        shark_r = sr
        shark_c = sc                                    # 상어 위치 갱신
        arr[sr][sc] = 0                                 # 먹은 물고기는 공간에서 제거
        answer += shortest                              # 정답에 거리를 누적

print(answer)
