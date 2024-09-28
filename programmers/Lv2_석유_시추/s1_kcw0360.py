from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[0] * m for _ in range(n)]
    oils = {}
    num = 1
    for i in range(m):
        for j in range(n):
            if land[j][i] != 0 and visited[j][i] == 0:
                temp = 1
                land[j][i] = num
                visited[j][i] = 1
                nxt = deque()
                nxt.append([j, i])

                while nxt:
                    y, x = nxt.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if (0 > ny or ny >= n) or (0 > nx or nx >= m) or land[ny][nx] != 1 or visited[ny][nx] != 0:
                            continue

                        temp += 1
                        visited[ny][nx] = 1
                        land[ny][nx] = num
                        nxt.append([ny, nx])

                oils[num] = temp
                num += 1

        check = set()
        for a in range(n):
            if land[a][i]:
                check.add(land[a][i])

        oil = 0
        for c in check:
            oil += oils[c]

        answer = max(answer, oil)

    return answer
