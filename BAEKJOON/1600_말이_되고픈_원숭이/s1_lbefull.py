from collections import deque


def bfs():
    Q = deque()
    Q.append((0, 0, 0))
    while Q:                                                                # BFS 탐색
        r, c, cnt = Q.popleft()                                             # 인접한 4칸을 탐색하여
        for d in range(4):                                                  # 현재 말처럼 이동한 횟수 cnt를 유지하며
            nr = r + dr[d]                                                  # 방문하지 않고 평지인 곳을 방문
            nc = c + dc[d]
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][cnt] == 100000 and not arr[nr][nc]:
                visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                Q.append((nr, nc, cnt))

        if cnt >= K: continue                                               # 더 이상 말처럼 움직일 수 없다면 다음반복

        for d in range(8):                                                  # 말처럼 이동
            nr = r + hr[d]                                                  # 이동할 곳이 말처럼 이동한 횟수 + 1로는 방문하지 않았고 평지이면 방문
            nc = c + hc[d]
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][cnt + 1] == 100000 and not arr[nr][nc]:
                visited[nr][nc][cnt + 1] = visited[r][c][cnt] + 1
                Q.append((nr, nc, cnt + 1))


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
hr = [2, 1, -1, -2, -2, -1, 1, 2]
hc = [-1, -2, -2, -1, 1, 2, 2, 1]
visited = [[[100000] * (K + 1) for c in range(W)] for r in range(H)]        # 말처럼 이동한 횟수에 따라 visited를 따로 저장
for i in range(K + 1):
    visited[0][0][i] = 0

bfs()
answer = min(visited[-1][-1])
if answer == 100000: answer = -1
print(answer)
