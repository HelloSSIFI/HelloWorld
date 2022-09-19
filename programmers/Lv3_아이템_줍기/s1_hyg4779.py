from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 두배로 늘려줌
    MAX = 20
    field = [[5]*MAX for _ in range(MAX)]

    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)

        # 테두리는 1 내부는 0으로 바꿔줌
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0

                # 겹치는 부분에 이미 0이면 테두리를 그리지 않고, 0이 아닐때만 테두리를 그림
                elif field[i][j] != 0:
                    field[i][j] = 1


    direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    Q = deque([(characterX*2, characterY*2)])
    visit = [[0]*MAX for _ in range(MAX)]
    visit[characterX*2][characterY*2] = 1

    while Q:
        x, y = Q.popleft()

        if x == itemX*2 and y == itemY*2:
            answer = (visit[x][y]-1)//2
            break

        for d in direct:
            nx, ny = x+d[0], y+d[1]
            # 방문 안한 테두리만 이동
            if visit[nx][ny] == 0 and field[nx][ny] == 1:
                Q.append((nx, ny))
                visit[nx][ny] = visit[x][y]+1


    for line in field:
        print(*line)
    return answer