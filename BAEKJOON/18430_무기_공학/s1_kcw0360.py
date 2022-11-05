import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0


def dfs(idx, total):
    global answer
    if idx == N*M:    # 모두 확인한 경우
        answer = max(answer, total)
        return

    y, x = idx // M, idx % M    # 현재 중심이 되는 좌표

    # 현재 좌표가(중심)이 사용되지 않은 경우, 부메랑을 만들 수 있는 4가지 모양을 모두 체크
    if visited[y][x] == 0:
        if y+1 < N and 0 <= x-1 and visited[y+1][x] == 0 and visited[y][x-1] == 0:
            visited[y][x] = 1
            visited[y+1][x] = 1
            visited[y][x-1] = 1
            dfs(idx+1, total+arr[y][x]*2+arr[y+1][x]+arr[y][x-1])
            visited[y][x] = 0
            visited[y+1][x] = 0
            visited[y][x-1] = 0

        if 0 <= y-1 and 0 <= x-1 and visited[y-1][x] == 0 and visited[y][x-1] == 0:
            visited[y][x] = 1
            visited[y-1][x] = 1
            visited[y][x-1] = 1
            dfs(idx+1, total+arr[y][x]*2+arr[y-1][x]+arr[y][x-1])
            visited[y][x] = 0
            visited[y-1][x] = 0
            visited[y][x-1] = 0

        if y+1 < N and x+1 < M and visited[y+1][x] == 0 and visited[y][x+1] == 0:
            visited[y][x] = 1
            visited[y+1][x] = 1
            visited[y][x+1] = 1
            dfs(idx+1, total+arr[y][x]*2+arr[y+1][x]+arr[y][x+1])
            visited[y][x] = 0
            visited[y+1][x] = 0
            visited[y][x+1] = 0

        if 0 <= y-1 and x+1 < M and visited[y-1][x] == 0 and visited[y][x+1] == 0:
            visited[y][x] = 1
            visited[y-1][x] = 1
            visited[y][x+1] = 1
            dfs(idx+1, total+arr[y][x]*2+arr[y-1][x]+arr[y][x+1])
            visited[y][x] = 0
            visited[y-1][x] = 0
            visited[y][x+1] = 0

    dfs(idx+1, total)


dfs(0, 0)
print(answer)