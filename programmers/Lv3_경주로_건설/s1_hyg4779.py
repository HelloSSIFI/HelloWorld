from collections import deque


def solution(board):
    # 북 동 남 서
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    n = len(board)
    answer = 1000*n*n

    # 방문한 곳 행, 열, 방향
    visit = [[[500*n*n]*4 for _ in range(n)] for _ in range(n)]
    visit[0][0] = [0, 0, 0, 0]

    queue = deque([])
    # 행, 열, 진행방향, 금액
    # 첫 이동: 남, 동 2가지
    for i in [1, 2]:
        nx, ny = 0 + dx[i], 0 + dy[i]
        if board[nx][ny] == 0:
            visit[nx][ny][i] = 100
            queue.append((nx, ny, i, 100))

    while queue:
        r, c, idx, res = queue.popleft()

        # 가지치기
        if res > answer:
            continue

        # 종착점
        if r == n-1 and c == n-1:
            if answer > res:
                answer = res
            continue

        for j in range(4):
            nr, nc = r + dx[j], c + dy[j]
            # cost: 현재값 + 도로비용 (+ 방향 다르다면 코너 값)
            cost = res + 100 if idx == j else res + 600

            # 현재 이동 방향으로 탐색한 적이 없는 곳 추가
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and visit[nr][nc][j] > cost:
                visit[nr][nc][j] = cost
                queue.append((nr, nc, j, cost))



    return answer