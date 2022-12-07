from collections import deque


def solution(board):
    N = len(board)
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]                                                                    # 가로방향일 때, 세로방향일 때, 해당 좌표 방문 시간을 저장
    visited[0][1][0] = 1                                                                                                        # (0, 1)의 가로방향을 1초로 표시
    Q = deque([[0, 1, 0]])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while Q:                                                                                                                    # BFS 탐색
        r, c, hv = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if hv == 0:                                                                                                         # 가로방향일 때
                if 0 <= nr < N and 1 <= nc < N and board[nr][nc] == board[nr][nc - 1] == visited[nr][nc][hv] == 0:              # 이동 후에 로봇이 차지하는 두 칸이 벽이 아니라면
                    visited[nr][nc][hv] = visited[r][c][hv] + 1                                                                 # 해당 로봇의 오른쪽 좌표에 시간을 표시하고
                    Q.append([nr, nc, hv])                                                                                      # Q에 넣어줌
            else:                                                                                                               # 세로 방향일 때도 가로방향과 마찬가지
                if 1 <= nr < N and 0 <= nc < N and board[nr][nc] == board[nr - 1][nc] == visited[nr][nc][hv] == 0:
                    visited[nr][nc][hv] = visited[r][c][hv] + 1
                    Q.append([nr, nc, hv])

        if hv == 0:                                                                                                             # 방향을 돌리는 경우
            nhv = 1                                                                                                             # 먼저 가로방향일 경우
            for nr, nc in [[r + 1, c], [r + 1, c - 1], [r - 1, c], [r - 1, c - 1]]:                                             # 왼쪽을 축으로 2방향, 오른쪽을 축으로 2방향 총 4가지 회전이 가능
                mr = max(r, nr)                                                                                                 # 회전 후 로봇이 차지하는 r 좌표중 큰 좌표를 mr로 표시
                if 0 <= nr < N and board[nr][c] == board[nr][c - 1] == visited[mr][nc][nhv] == 0:                               # 회전하는 방향이 벽이 아니라면
                    visited[mr][nc][nhv] = visited[r][c][hv] + 1                                                                # 회전하는 좌표에 시간을 표시 후 Q에 넣어줌
                    Q.append([mr, nc, nhv])
        else:                                                                                                                   # 세로방향도 가로방향과 마찬가지
            nhv = 0
            for nr, nc in [[r, c + 1], [r - 1, c + 1], [r, c - 1], [r - 1, c - 1]]:
                mc = max(c, nc)
                if 0 <= nc < N and board[r][nc] == board[r - 1][nc] == visited[nr][mc][nhv] == 0:
                    visited[nr][mc][nhv] = visited[r][c][hv] + 1
                    Q.append([nr, mc, nhv])

    answer = min(visited[-1][-1])                                                                                               # 맨 오른쪽 아래 좌표의 시간을 탐색하여
    if not answer: answer = max(visited[-1][-1])                                                                                # 0이 아닌 최소값을 정답으로 지정
    return answer - 1                                                                                                           # 초기값을 1로 설정하였으므로 1을 빼줌


# print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
