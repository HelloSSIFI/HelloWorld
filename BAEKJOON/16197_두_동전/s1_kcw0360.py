from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    coins = deque()
    coins.append([start[0], start[1], start[2], start[3], 0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while coins:
        y1, x1, y2, x2, cnt = coins.popleft()

        if cnt >= 10:    # 10번 보다 많이 눌러야 하면 fail
            break

        for k in range(4):    # 이동
            dy1 = y1 + dy[k]
            dx1 = x1 + dx[k]
            dy2 = y2 + dy[k]
            dx2 = x2 + dx[k]

            if 0 <= dy1 < N and 0 <= dx1 < M and 0 <= dy2 < N and 0 <= dx2 < M:    # 범위 이내의 경우에서
                if board[dy1][dx1] == "#":    # 벽을 만난 경우 움직이지 않으므로 좌표 복구
                    dy1 = y1
                    dx1 = x1
                if board[dy2][dx2] == "#":
                    dy2 = y2
                    dx2 = x2
                coins.append([dy1, dx1, dy2, dx2, cnt + 1])    # 벽이 있었지만 버튼은 눌렀기 때문에 카운트는 함

            # 둘 중 하나만 떨어진 경우
            elif 0 <= dy1 < N and 0 <= dx1 < M:
                return cnt + 1

            elif 0 <= dy2 < N and 0 <= dx2 < M:
                return cnt + 1

            else:    # 둘 다 떨어진 경우는 무시
                continue

    return -1


N, M = map(int, input().split())    # N: 세로, M: 가로
board = []
temp = []
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'o':
            temp.extend([i, j])

print(bfs(temp))