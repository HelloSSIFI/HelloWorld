from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]


def bfs(i, j):
    q = deque()
    q.append([i, j, 0, 0])    # y좌표, x좌표, 현재 가지고 있는 열쇠, 이동거리
    visited = [[[0]*64 for _ in range(M)] for _ in range(N)]    # visited[y][x][key]
    visited[i][j][0] = 1    # 출발 지점

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b, key, dis = q.popleft()

        if maze[a][b] == '1':    # 도착 지점인 경우
            return dis

        for k in range(4):    # 이동
            y = a + dy[k]
            x = b + dx[k]

            if 0 <= y < N and 0 <= x < M:    # 이동하는 곳이 미로 내부
                if visited[y][x][key] == 0:    # 아직 해당 열쇠들을 가지고 방문하지 않은 경우
                    if maze[y][x] in ['0', '1', '.']:    # 이동할 수 있는 곳 체크
                        visited[y][x][key] = 1    # 현재 좌표 방문시 가지고 있는 열쇠들값에 체크
                        q.append([y, x, key, dis+1])    # q에 이동거리 +1 후 추가

                    elif maze[y][x] in ['a', 'b', 'c', 'd', 'e', 'f']:    # 이동하는 곳에 열쇠가 있는 경우
                        tmp = key | (1 << (ord(maze[y][x]) - ord('a')))    # 열쇠 추가
                        visited[y][x][tmp] = 1
                        q.append([y, x, tmp, dis+1])

                    elif maze[y][x] in ['A', 'B', 'C', 'D', 'E', 'F']:    # 이동하는 곳에 문이 있는 경우
                        check = key & (1 << (ord(maze[y][x]) - ord('A')))    # 문이랑 대응하는 열쇠가 있는지 확인
                        if check:    # 열쇠가 존재
                            visited[y][x][key] = 1
                            q.append([y, x, key, dis+1])

    return -1


# 출발 지점 찾기
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            print(bfs(i, j))