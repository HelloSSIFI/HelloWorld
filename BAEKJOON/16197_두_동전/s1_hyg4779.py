from collections import deque

N, M = map(int, input().split())
arr = [tuple(input()) for _ in range(N)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
coin = []

for i in range(N):
    for j in range(M):
        if arr[i][j]=='o':
            coin.append([i, j])

coin = deque([(coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0)])


def bfs():
    while coin:
        r1, c1, r2, c2, cnt = coin.popleft()

        if cnt >= 10:return -1

        for d in direct:
            nr1, nc1 = r1+d[0], c1+d[1]
            nr2, nc2 = r2+d[0], c2+d[1]

            if 0 <= nr1 < N and 0 <= nc1 < M and 0 <= nr2 < N and 0 <= nc2 < M:
                if arr[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if arr[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2
                coin.append([nr1, nc1, nr2, nc2, cnt+1])

            elif 0 <= nr1 < N and 0 <= nc1 < M:
                return cnt+1
            elif 0 <= nr2 < N and 0 <= nc2 < M:
                return cnt+1
            else:
                continue


print(bfs())