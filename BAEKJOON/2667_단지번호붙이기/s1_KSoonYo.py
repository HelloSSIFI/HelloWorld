import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())
village = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

q = []

# 상 하 좌 우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if visited[i][j] or not village[i][j]:
            continue

        temp_q = deque()
        temp_q.append((i, j))
        visited[i][j] = True
        cnt = 1
        while temp_q:
            apartment_location = temp_q.popleft()

            for dir_idx in range(4):
                next_x = apartment_location[0] + dx[dir_idx]
                next_y = apartment_location[1] + dy[dir_idx]

                if 0 <= next_x < N and 0 <= next_y < N:
                    if not visited[next_x][next_y] and village[next_x][next_y]:
                        visited[next_x][next_y] = True
                        temp_q.append((next_x, next_y))
                        cnt += 1
        heapq.heappush(q, cnt)

print(len(q))
while q:
    house_cnt = heapq.heappop(q)
    print(house_cnt)
