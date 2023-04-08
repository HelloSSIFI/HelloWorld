from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def search(start, goal):
        visited = [[0]*m for _ in range(n)]
        q = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = 1

        while q:
            a, b, cnt = q.popleft()

            if (a, b) == goal:
                return cnt

            for k in range(4):
                y = a + dy[k]
                x = b + dx[k]

                if 0 <= y < n and 0 <= x < m and maps[y][x] != 'X' and visited[y][x] == 0:
                    visited[y][x] = 1
                    q.append((y, x, cnt+1))

        return 0

    check = [(), (), ()]    # 좌표 저장 [시작 지점, 레버, 출구]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                check[0] = (i, j)
            elif maps[i][j] == 'L':
                check[1] = (i, j)
            elif maps[i][j] == 'E':
                check[2] = (i, j)

    result1 = search(check[0], check[1])    # 출발 지점 -> 레버
    result2 = search(check[1], check[2])    # 레버 -> 출구

    if result1 and result2:    # 둘 다 도착하는 경우에만 최종적으로 탈출이 가능
        return result1 + result2
    else:
        return -1