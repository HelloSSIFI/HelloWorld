from collections import deque


def solution(board):
    N = len(board)
    cost = [[[10000000] * 2 for _ in range(N)] for _ in range(N)]           # 각 좌표까지의 비용을 큰 값으로 초기화
    Q = deque()
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    cost[0][0][0] = cost[0][0][1] = 0                                       # cost의 좌표에 각각 0은 세로방향 1은 가로방향 비용을 저장할 예정
    Q.append([0, 0, 0])                                                     # Q에는 좌표와 이전에 움직인 방향을 넣어줌

    while Q:                                                                # BFS 탐색
        r, c, p = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:           # 좌표를 벗어나지 않고 벽이 아니라면
                add = 600                                                   # 도로 건설 비용(add) 계산
                if r == c == 0 or p % 2 == d % 2:                           # 시작점이거나 직선도로(이전 방향과 같은 방향)이면 추가비용은 100
                    add = 100                                               # 코너라면 추가비용은 600
                if cost[nr][nc][d % 2] > cost[r][c][p % 2] + add:           # 이전 좌표와 방향에 저장된 비용(cost[r][c][p % 2])에 추가비용(add)을 더한 값이 
                    cost[nr][nc][d % 2] = cost[r][c][p % 2] + add           # 이동할 좌표와 방향에 저장된 비용(cost[nr][nc][d % 2])보다 작을경우 갱신
                    Q.append([nr, nc, d])

    return min(cost[-1][-1])


# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
