from collections import deque


def solution(game_board, table):
    # 블록 빈칸 채우기
    def fill():

        for x in range(a):
            for y in range(b):
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] + now[x][y] == 1:
                    if now[x][y] == 1:
                        board[ni][nj] = 2
                        block.append((ni, nj))
                else:
                    return False
        return True

    # 현재 블록 주변 빈칸 탐색
    def isblank():
        for r, c in block:
            for d in range(4):
                nr, nc = r + dx[d], c + dy[d]
                if 0 <= nr < n and 0 <= nc < n:
                    # 주변에 빈칸이 있다면 False
                    if board[nr][nc] == 0:
                        return False
        return True


    answer = 0
    n, shapes = len(table), []
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    visit = [[0 for _ in range(n)] for _ in range(n)]


    # table의 도형들 추출
    for i in range(n):
        for j in range(n):
            if table[i][j] and visit[i][j] == 0:
                visit[i][j] = 1
                Q, el = deque([(i, j)]), [(0, 0)]
                min_x, min_y, max_x, max_y = i, j, i, j

                while Q:
                    r, c = Q.popleft()

                    for d in range(4):
                        nr, nc = r + dx[d], c + dy[d]
                        if 0 <= nr < n and 0 <= nc < n and table[nr][nc] and visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            el.append((nr-i, nc-j))
                            Q.append((nr, nc))
                            min_x, min_y = min(min_x, nr), min(min_y, nc)
                            max_x, max_y = max(max_x, nr), max(max_y, nc)

                shape = [[0]*(max_y-min_y+1) for _ in range(max_x-min_x+1)]

                for ni, nj in el:
                    shape[ni][nj] = 1

                shapes.append(shape)

    # 도형의 개수
    m = len(shapes)

    for k in range(m):
        now = shapes[k]
        flag = False

        # 회전 까지 총 4번 탐색
        for _ in range(4):
            # 도형의 세로 가로 길이
            a, b = len(now), len(now[0])
            if flag:break

            # game_board의 빈칸 탐색
            for i in range(n-a+1):
                if flag:break

                for j in range(n-b+1):

                    # 게임판 복사
                    board = [row[:] for row in game_board]
                    # 현재 도형의 인덱스 담음
                    block = []

                    # 도형이 꽉 차면
                    if fill():
                        # 도형을 모두 채웠으면 빈칸 검사
                        if isblank():
                            answer += len(block)
                            game_board = board
                            flag = True
                    if flag:break
            # 도형 회전
            now = list(zip(*now[::-1]))

    return answer

print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))

print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))