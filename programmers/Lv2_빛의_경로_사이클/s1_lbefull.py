import sys
sys.setrecursionlimit(1000001)

dr = [-1, 0, 1, 0]                              # 시계방향
dc = [0, 1, 0, -1]                              # 상우하좌


def dfs(r, c, d, cnt, cycle, grid):             # 확인해야 할 위치와 방향, 사이클 번호와 길이를 받아옴
    visited[r][c][d] = cnt                      # 현재 방향을 사이클 번호로 방문표시
    nr = (r + dr[d]) % N                        # 가야할 방향의 좌표와 방향을 구해줌
    nc = (c + dc[d]) % M
    nd = d
    if grid[nr][nc] == 'R':
        nd = (d + 1) % 4
    elif grid[nr][nc] == 'L':
        nd = (d - 1) % 4
    
    if visited[nr][nc][nd] == cnt:              # 가야할 방향이 현재 사이클에서 이미 방문한 곳이면
        answer.append(cycle)                    # 사이클 길이를 추가 후 리턴
        return
    
    dfs(nr, nc, nd, cnt, cycle + 1, grid)       # 아직 방문하지 않았다면 사이클 길이+1 후 재귀


def solution(grid):
    global visited, answer, N, M
    answer = []
    N = len(grid)
    M = len(grid[0])
    visited = [[[0] * 4 for _ in range(M)] for i in range(N)]
    
    cnt = 0
    for r in range(N):                              # 그리드의 4방향을 탐색하여
        for c in range(M):                          # 아직 사이클이 돌지 않았으면
            for d in range(4):                      # 재귀 시작
                if not visited[r][c][d]:
                    cnt += 1
                    dfs(r, c, d, cnt, 1, grid)
    answer.sort()
    return answer

# print(solution(["SL","LR"]))
