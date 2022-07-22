"""
map 을 바꿔줄 필요 없음
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(c):
    queue = deque()
    queue.append(c)

    while queue:
        coins = queue.popleft()

        if coins[0][2] >= 10:
            return -1

        for d in di:
            temp = []
            for coin in coins:
                i, j, cnt = coin[0], coin[1], coin[2]
                next_i, next_j = i + d[0], j + d[1]

                if 0 <= next_i < N and 0 <= next_j < M:
                    if coin_map[next_i][next_j] == "#":
                        next_i, next_j = i, j
                    temp.append([next_i, next_j, cnt + 1])

            if len(temp) == 1:
                return cnt + 1
            elif not temp:
                continue
            else:
                queue.append(temp)
    return -1


N, M = map(int, input().split())
coin_map = [list(input().rstrip()) for _ in range(N)]
coins = []
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for r in range(N):
    for c in range(M):
        if coin_map[r][c] == 'o':
            coins.append([r, c, 0])

print(bfs(coins))