N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

visited[0][1] = [1, 0, 0]                                           # 가로, 대각선, 세로 방향의 경우의 수를 저장 
for r in range(N):
    for c in range(N):
        for d in range(3):                                          # 각각의 방향마다 반복
            if d in [0, 1]:                                         # r, c+1 칸에 가로 방향으로 진입할 때의 경우를 구함
                if c + 1 < N and not arr[r][c + 1]:                 # 이전에 가로 또는 대각선이면서 벽이 아니면
                    visited[r][c + 1][0] += visited[r][c][d]        # 이전 가로, 대각선 경우의 수를 더해줌
            
            if d in [1, 2]:                                         # 세로도 마찬가지
                if r + 1 < N and not arr[r + 1][c]:                 # 대각선의 경우 이전 방향에 관계없이 모두 진입가능
                    visited[r + 1][c][2] += visited[r][c][d]
            
            if r + 1 < N and c + 1 < N and not arr[r + 1][c] and not arr[r][c + 1] and not arr[r + 1][c + 1]:
                visited[r + 1][c + 1][1] += visited[r][c][d]

print(sum(visited[-1][-1]))
