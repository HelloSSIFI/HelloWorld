from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

while answer < 2000:
    visit = [[0]*n for _ in range(n)]
    unions = list()
    for i in range(n):
        for j in range(n):
            # 방문 안한 나라라면
            if visit[i][j] == 0:
                # 방문 처리
                visit[i][j] = 1
                # 현재 나라의 인구수 & 누적할 연합 인구의 수
                now = field[i][j]
                Q = deque([(i, j, now)])
                union = list()
                while Q:
                    # 현재 나라 위치, 현재 나라의 인구 수
                    x, y, std = Q.popleft()
                    # 연합에 추가
                    union.append((x, y))

                    # 4방향 탐색
                    for d in direct:
                        nx, ny = x+d[0], y+d[1]
                        # 방문 안했고, 현재 국가와 인구 수 차이가 l이상 r 이하라면
                        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                            if l <= abs(field[nx][ny]-std) <= r:
                                visit[nx][ny] = 1
                                now += field[nx][ny]
                                Q.append((nx, ny, field[nx][ny]))

                # 연합의 수가 1 이상이라면 연합 국가에 추가
                if len(union) > 1:
                    unions.append((union, now))

    if unions:
        answer += 1
        for uni in unions:
            # 그룹과 그룹의 총 인구수
            tmp, people = uni
            # 인구 값 = 총 인구수/국가 수
            val = people//len(tmp)
            for x, y in tmp:
                field[x][y] = val
    else:
        break

print(answer)