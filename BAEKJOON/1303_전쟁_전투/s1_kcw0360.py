import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

war = [list(input()) for _ in range(M)]

friendly = 0
enemy = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(i, j, team):
    q = deque()
    q.append((i, j))
    war[i][j] = 0
    cnt = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]

            if 0 <= x < N and 0 <= y < M and war[y][x] == team:
                war[y][x] = 0
                q.append((y, x))
                cnt += 1

    return cnt**2


for i in range(M):
    for j in range(N):
        if war[i][j] == 'W':
            friendly += bfs(i, j, 'W')
        elif war[i][j] == 'B':
            enemy += bfs(i, j, 'B')

print(friendly, enemy)
