N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

for r in range(N):                                  # 게임판 순회
    for c in range(N):
        if visited[r][c] and arr[r][c]:             # 방문한 적이 있는 곳이고 점프할 수 있으면
            nr = r + arr[r][c]                      # 점프해서 이동하는 위치를 구해서
            nc = c + arr[r][c]

            if nr < N:                              # 현재 경우의 수를 더해줌
                visited[nr][c] += visited[r][c]
            
            if nc < N:
                visited[r][nc] += visited[r][c]

print(visited[-1][-1])
