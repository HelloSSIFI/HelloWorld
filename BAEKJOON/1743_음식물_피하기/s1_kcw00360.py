from collections import deque

N, M, K = map(int, input().split())    # N: 세로 길이, M: 가로 길이, K: 음식물 쓰레기의 개수
space = [[0]*M for _ in range(N)]    # 공간
visited = [[0]*M for _ in range(N)]    # 방문지 체크
result = []    # 쓰레기 크기 저장

for _ in range(K):    # 음식물 쓰레기 배치
    a, b = map(int, input().split())
    space[a-1][b-1] = 1    # 음식물 쓰레기가 위치한 곳 표시


def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    cnt = 1    # 쓰레기 개수

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        for k in range(4):
            y = now[0] + dy[k]
            x = now[1] + dx[k]
            if 0 <= y < N and 0 <= x < M and space[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = 1
                cnt += 1
                q.append([y, x])

    return cnt


for i in range(N):
    for j in range(M):
        if space[i][j] == 1 and visited[i][j] == 0:
            result.append(bfs([i, j]))

print(max(result))
