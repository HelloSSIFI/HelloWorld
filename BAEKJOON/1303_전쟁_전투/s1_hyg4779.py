from collections import deque
import sys

N, M = map(int, input().split())
arr = [list(sys.stdin.readline()) for _ in range(M)]

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visit = [[False]*N for _ in range(M)]

power = {'W': 0, 'B': 0}


def bfs(color, i, j):

    queue = deque([(i, j)])
    visit[i][j] = True
    cnt = 0
    while queue:
        ni, nj = queue.popleft()
        cnt += 1
        for d in direct:
            si, sj = ni+d[0], nj+d[1]
            if 0 <= si < M and 0 <= sj < N and not visit[si][sj] and arr[si][sj] == color:
                visit[si][sj] = True
                queue.append((si, sj))



    # print(color, cnt)
    power[color] += cnt**2


for r in range(M):
    for c in range(N):
        if not visit[r][c]:
            bfs(arr[r][c], r, c)

print(f'{power["W"]} {power["B"]}')