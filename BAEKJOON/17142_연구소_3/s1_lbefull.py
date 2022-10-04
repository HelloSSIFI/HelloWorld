from itertools import combinations
from collections import deque


def bfs(target):
    global answer
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    for r, c in target:                                                                         # 현재 조합에서의 바이러스 위치를
        Q.append((r, c))                                                                        # Q에 담아주고
        visited[r][c] = 1                                                                       # 바이러스가 퍼졌다는 표시를 남겨줌

    while Q:                                                                                    # BFS 탐색
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))

    flag = True
    max_sec = 0
    for r in range(N):
        for c in range(N):                                                                      # BFS 탐색이 끝난 후
            if visited[r][c] == 0 and arr[r][c] == 0:                                           # 바이러스가 퍼지지 않은 곳이 있다면
                flag = False                                                                    # answer을 갱신하지 않음
            if arr[r][c] == 0 and visited[r][c] - 1 > max_sec:                                  # 퍼진 거리 최대값을 구해줌
                max_sec = visited[r][c] - 1

    if flag:                                                                                    # 바이러스가 전부 퍼졌다면
        answer = min(answer, max_sec)                                                           # answer 갱신


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 2501
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

virus = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:                  # 초기 바이러스 위치를 virus에 저장
            virus.append((r, c))

for v in combinations(virus, M):            # virus 중 M 개의 조합을 만들어서
    bfs(v)                                  # 현재 조합 v로 bfs 탐색

if answer == 2501:                          # answer이 갱신이 되지 않았다면
    answer = -1                             # 바이러스 퍼뜨리는데 실패한 것이므로 -1

print(answer)
