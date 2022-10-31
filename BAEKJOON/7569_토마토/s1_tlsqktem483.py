from collections import deque


def tomato_cnt():
    t_list = []
    cnt = 0
    for idx in range(H):
        for i in range(N):
            for j in range(M):
                if graph[idx][i][j] == 1:
                    t_list.append([idx, i, j, 0])
                elif graph[idx][i][j] == 0:
                    cnt += 1
    return t_list, cnt


def bfs(input_list):
    global ans, graph

    q = deque()
    visited = [[[False]*M for _ in range(N)] for _ in range(H)]
    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for arr in input_list:
        q.append(arr)
        visited[arr[0]][arr[1]][arr[2]] = True

    while q:
        idx, i, j, day = q.popleft()
        ans = max(ans, day)

        for di in d:
            n_idx, ni, nj = idx + di[0], i + di[1], j + di[2]
            if 0 <= n_idx < H and 0 <= ni < N and 0 <= nj < M and not visited[n_idx][ni][nj] and graph[n_idx][ni][nj] == 0:
                visited[n_idx][ni][nj] = True
                q.append([n_idx, ni, nj, day+1])
                graph[n_idx][ni][nj] = 1


ans = 0
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

init, _ = tomato_cnt()
bfs(init)
_, flag = tomato_cnt()
if flag:
    print(-1)
else:
    print(ans)