from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 길이를 2배 해서 찾아준다. 원래 길이로 할 경우 bfs로 탐색시 겹치는 사각형에서
    # 사각형 테두리 쪽으로 가는 것이 아닌 가까운쪽으로 이동하기 때문에 이를 방지
    field = [[-11]*102 for _ in range(102)]    # 테두리 인지 확인
    visited = [[0]*102 for _ in range(102)]    # 방문 체크
    q = deque()
    q.append((characterY*2, characterX*2))
    visited[characterY*2][characterX*2] = 0

    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if y1 < i < y2 and x1 < j < x2:    # 직사각형 내부
                    field[i][j] = 0
                elif field[i][j] != 0:    # 직사각형 테두리
                    field[i][j] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()

        if (a, b) == (itemY*2, itemX*2):
            return visited[a][b] // 2    # 길이를 2배 증가해서 찾았기 때문에 2를 나눠준다

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]

            if field[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = visited[a][b] + 1
                q.append((y, x))