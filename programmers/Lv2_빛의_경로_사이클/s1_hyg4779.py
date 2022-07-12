# 시작점, 현재 (r, c), 사이클 길이


dt = [(-1, 0), (0, 1), (1, 0), (0, -1)]         # 시계방향 탐색

def solution(grid):

    global visit, N, M

    ans = []
    N, M = len(grid), len(grid[0])                  # 세로 가로 길이
    visit = [[[False]*4 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(4):
                if not visit[i][j][k]:
                    res = dfs(i, j, k, grid, visit)
                    if res:
                        ans.append(res)

    ans.sort()
    return ans


def dfs(sr, sc, sd, grid, visit):

    r, c, d = sr, sc, sd
    cnt = 0
    visit[sr][sc][sd] = True

    while True:
        r, c = (r+dt[d][0])%N, (c+dt[d][1])%M
        cnt += 1

        if grid[r][c] == 'L':
            d = (d-1)%4
        elif grid[r][c] == 'R':
            d = (d+1)%4

        if visit[r][c][d]:
            if (r, c, d) == (sr, sc, sd):
                return cnt
            else:
                return 0

        visit[r][c][d] = True

print(solution(["SL", "LR"]))