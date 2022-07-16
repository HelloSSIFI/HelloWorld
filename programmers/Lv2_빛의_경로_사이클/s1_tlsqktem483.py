def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # 상 우 하 좌

    for r in range(n):
        for c in range(m):
            for dir in range(4):
                if not visited[r][c][dir]:
                    i, j, d = r, c, dir
                    cnt = 0
                    while not visited[i][j][d]:
                        visited[i][j][d] = True
                        cnt += 1
                        (di, dj) = direction[d]
                        i, j = (i + di) % n, (j + dj) % m

                        if grid[i][j] == "R":
                            d = (d + 1) % 4
                        elif grid[i][j] == "L":
                            d = (d - 1) % 4
                    answer.append(cnt)

    return sorted(answer)

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))