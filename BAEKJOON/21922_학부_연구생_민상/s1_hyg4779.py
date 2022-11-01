from collections import deque
import sys
input = sys.stdin.readline


def in_frame(r, c):
    return True if 0 <= r < n and 0 <= c < m else False

n, m = map(int, input().split())
room = []
aircon = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):

        if line[j] == 9:
            aircon.append((i, j))

    room.append(line)

# 상하좌우
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
answer = 0

# 굴절방향
turn = {
    1: {0: 0, 1: 1},
    2: {2: 2, 3: 3},
    3: {0: 3, 1: 2, 2: 1, 3: 0},
    4: {0: 2, 1: 3, 2: 0, 3: 1}
}

visit = [[[0]*4 for _ in range(m)] for _ in range(n)]


Q = deque([])
for r, c in aircon:
    for i in range(4):
        Q.append((r, c, i))
        visit[r][c][i] = 1

    answer += 1

while Q:
    r, c, idx = Q.popleft()

    # 다음 바람 위치
    nr, nc = r+dr[idx], c+dc[idx]

    # 방 안이고, 해당 방향으로 바람이 지나간 적이 없다면
    if in_frame(nr, nc):

        if sum(visit[nr][nc]) == 0:
            answer += 1

        # 해당 방향으로 바람이 지나간 적이 없으면 탐색 있으면 continue
        if visit[nr][nc][idx] == 0:
            visit[nr][nc][idx] = 1

            # 물건이 있다면
            if 1 <= room[nr][nc] < 5:
                thing = room[nr][nc]
                head = turn[thing].get(idx, 100)
                if head == 100:
                    pass
                else:
                    Q.append((nr, nc, head))

            # 물건이 없다면
            else:
                Q.append((nr, nc, idx))

print(answer)