from collections import deque


def bfs(q):

    while q:
        i, j = q.popleft()

        for idx in range(4):
            d_idx = idx
            di = d[d_idx]
            ni, nj = i + di[0], j + di[1]

            while 0 <= ni < N and 0 <= nj < M:
                visited[ni][nj] = True

                if graph[ni][nj] == 9:
                    break

                elif graph[ni][nj] == 3:
                    if d_idx in [0, 2]:
                        d_idx = (d_idx - 1) % 4
                    else:
                        d_idx = (d_idx + 1) % 4

                elif graph[ni][nj] == 4:
                    if d_idx in [0, 2]:
                        d_idx = (d_idx + 1) % 4
                    else:
                        d_idx = (d_idx - 1) % 4

                elif (graph[ni][nj] == 1 and d_idx not in [0, 2]) or (graph[ni][nj] == 2 and d_idx not in [1, 3]):
                    break

                di = d[d_idx]
                ni, nj = ni + di[0], nj + di[1]


ans = 0
N, M = map(int, input().split())
graph = []
visited = [[False]*M for _ in range(N)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = deque()

for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for j in range(M):
        if arr[j] == 9:
            queue.append([i, j])
            visited[i][j] = True

bfs(queue)

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1

print(ans)