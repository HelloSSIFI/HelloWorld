import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
shark = {i: [] for i in range(1, M+1)}
graph = []
scent = [[(0, 0)]*N for _ in range(N)]
for i in range(N):
    graph_list = list(map(int, input().split()))
    graph.append(graph_list)
    for j in range(N):
        if graph_list[j]:
            shark[graph_list[j]].append([i, j])
            scent[i][j] = (graph_list[j], 0+K)
d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
directions = list(map(int, input().split()))
for i in range(M):
    shark[i+1][0].append(directions[i])
for i in range(1, M+1):
    for _ in range(4):
        shark[i].append(list(map(int, input().split())))

t = 0
num_shark = M
while t < 1001 and num_shark > 1:
    t += 1

    not_move = []
    # 이동
    for idx in shark.keys():
        i, j, d_idx = shark[idx][0]
        flag = False
        if [i, j] == [N, N]:
            continue
        for dir in shark[idx][d_idx]:
            di = d[dir]
            ni, nj = i + di[0], j + di[1]
            if 0 <= ni < N and 0 <= nj < N:
                if scent[ni][nj][1] < t:
                    shark[idx][0] = [ni, nj, dir]
                    graph[i][j], graph[ni][nj] = 0, graph[i][j]
                    scent[ni][nj] = (idx, t+K)
                    flag = True
                    break
                elif scent[ni][nj][1] == t+K:
                    num_shark -= 1
                    flag = True
                    if scent[ni][nj][0] > idx:
                        shark[scent[ni][nj][0]][0] = [N, N, dir]
                        scent[ni][nj][0] = (idx, t + K)
                        shark[idx][0] = [ni, nj, dir]
                        graph[i][j], graph[ni][nj] = 0, graph[i][j]
                    else:
                        shark[idx][0] = [N, N, dir]
                        graph[i][j] = 0
                    break
        if not flag:
            not_move.append(idx)
    for idx in not_move:
        i, j, d_idx = shark[idx][0]
        for dir in shark[idx][d_idx]:
            di = d[dir]
            ni, nj = i + di[0], j + di[1]
            if 0 <= ni < N and 0 <= nj < N:
                if scent[ni][nj][0] == idx:
                    shark[idx][0] = [ni, nj, dir]
                    graph[i][j], graph[ni][nj] = 0, graph[i][j]
                    scent[ni][nj] = (idx, t + K)
                    break

print(t if t < 1001 else -1)
