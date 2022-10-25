from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]


nr, nc = 0, 0
for a in range(N):
    for b in range(N):
        if arr[a][b] == 9:
            arr[a][b] = 0
            nr, nc = a, b                       # 상어위치 및 0 처리
            break

me, eat, ans = 2, 0, 0                          # 상어크기, 먹은 고기 수, 출력할 답
while True:
    Q = deque([(nr, nc)])
    feed = []                                   # 먹이 배열
    min_d = N*N                                 # 최단거리 초기화
    visit = [[0]*N for _ in range(N)]
    visit[nr][nc] = 1
    while Q:
        x, y = Q.popleft()


        if 0 != arr[x][y] < me:
            min_d = min(min_d, visit[x][y])
            feed.append((x, y))

        for d in direct:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < N and 0 <= dy < N and not visit[dx][dy] and arr[dx][dy] <= me:
                visit[dx][dy] = visit[x][y]+1
                Q.append((dx, dy))

    if feed:                                 # 먹을 수 있는 고기가 있을 때 반복
        r, c = N, N
        for i, j in feed:
            if visit[i][j] == min_d:
                if i < r:
                    r, c = i, j
                elif r == i and c > j:
                    c = j
        arr[r][c] = 0
        ans += visit[r][c]-1
        nr, nc = r, c
        eat += 1
        if eat == me:
            me += 1
            eat = 0

    else:                                       # 먹을 수 없다면 ans 출력
        print(ans)
        exit()