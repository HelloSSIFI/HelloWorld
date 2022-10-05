from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
answer = []
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])


def bfs(case):
    visited = [[0]*N for _ in range(N)]
    q = deque()
    for a, b in case:
        visited[a][b] = 1
        q.append([a, b])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]
            if 0 <= y < N and 0 <= x < N:
                if visited[y][x] == 0 and lab[y][x] != 1:    # 벽이 아닌 모든 곳은 퍼질수 있다.
                    visited[y][x] = visited[a][b] + 1
                    q.append([y, x])

    tmp = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                if visited[i][j] == 0:    # 빈 칸이지만 바이러스가 퍼지지 못한 경우 -1 return
                    return -1
                else:
                    tmp = max(tmp, visited[i][j])
    if tmp:
        return tmp - 1
    else:    # 시간이 0초 인경우
        return 0


for com in combinations(virus, M):    # 활성 바이러스 위치 경우의 수
    t = bfs(com)
    if t != -1:    # 모두 퍼진 경우만 answer에 추가
        answer.append(t)

if answer:    # 최소 시간
    print(min(answer))
else:    # 모두 퍼진 경우가 없다면 -1
    print(-1)