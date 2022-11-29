from collections import deque


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]    # 주사위
north, east, south, west = 0, 1, 2, 3
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def move_dice(nxt):
    if nxt == north:
        tmp = dice[0][1]
        for i in range(0, 3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp
    elif nxt == east:
        tmp = dice[1][2]
        for i in range(2, 0, -1):
            dice[1][i] = dice[1][i-1]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif nxt == south:
        tmp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i-1][1]
        dice[0][1] = tmp
    elif nxt == west:
        tmp = dice[1][0]
        for i in range(0, 2):
            dice[1][i] = dice[1][i+1]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp


def move(a, b, nxt):
    y = a + dy[nxt]
    x = b + dx[nxt]
    if not (0 <= y < N and 0 <= x < M):
        if nxt == east:
            nxt = west
        elif nxt == west:
            nxt = east
        elif nxt == north:
            nxt = south
        elif nxt == south:
            nxt = north
        y = a + dy[nxt]
        x = b + dx[nxt]

    move_dice(nxt)
    return y, x, nxt


def nxt_dir(y, x, nxt):
    if arr[y][x] > dice[3][1]:
        return nxt - 1 if nxt > 0 else west
    elif arr[y][x] < dice[3][1]:
        return (nxt + 1) % 4
    return nxt


def get_score(sy, sx):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append([sy, sx])
    visited[sy][sx] = 1
    cnt = 1

    while q:
        a, b = q.popleft()

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]
            if 0 <= y < N and 0 <= x < M and visited[y][x] == 0 and arr[y][x] == arr[sy][sx]:
                visited[y][x] = 1
                cnt += 1
                q.append([y, x])

    return cnt


y, x, nxt = 0, 0, east
answer = 0
while K:
    y, x, nxt = move(y, x, nxt)
    answer += get_score(y, x) * arr[y][x]
    nxt = nxt_dir(y, x, nxt)
    K -= 1

print(answer)