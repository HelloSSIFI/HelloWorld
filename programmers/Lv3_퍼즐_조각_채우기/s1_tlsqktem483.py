from collections import deque, defaultdict
from copy import deepcopy

def solution(game_board, table):
    ans = 0

    def make_table_group(r, c, idx, init=False):
        nonlocal is_visited

        q = deque()
        q.append([r, c])
        is_visited[r][c] = True
        table[r][c] = idx
        group = [[r, c]]

        while q:
            i, j = q.popleft()
            for di in d:
                ni, nj = i + di[0], j + di[1]
                flag = False

                if init and 0 <= ni < N and 0 <= nj < N and not is_visited[ni][nj] and table[ni][nj] == 1:
                    flag = True
                elif not init and 0 <= ni < N and 0 <= nj < N and not is_visited[ni][nj] and current[ni][nj] == idx:
                    flag = True

                if flag:
                    q.append([ni, nj])
                    group.append([ni, nj])
                    is_visited[ni][nj] = True
                    if init:
                        table[ni][nj] = idx

        group.sort()
        base = group[0][:]
        for idx in range(len(group)-1, -1, -1):
            group[idx][0], group[idx][1] = group[idx][0]-group[0][0], group[idx][1]-group[0][1]

        return group, base

    def make_game_group(r, c):
        nonlocal visited

        q = deque()
        q.append([r, c])
        visited[r][c] = True
        group = [[r, c]]

        while q:
            i, j = q.popleft()
            for di in d:
                ni, nj = i + di[0], j + di[1]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and game_board[ni][nj] == 0:
                    q.append([ni, nj])
                    group.append([ni, nj])
                    visited[ni][nj] = True

        group.sort()
        base = group[0][:]
        for idx in range(len(group)-1, -1, -1):
            group[idx][0], group[idx][1] = group[idx][0]-group[0][0], group[idx][1]-group[0][1]

        return group, base

    N = len(game_board)
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Indexing the Table
    block = defaultdict(list)
    is_visited = [[False] * len(game_board[0]) for _ in range(len(game_board))]
    block_idx = 2
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and not is_visited[i][j]:
                g, b = make_table_group(i, j, block_idx, True)
                block[block_idx].append([b, g])
                block_idx += 1

    current = deepcopy(table)
    for _ in range(3):
        current = list(map(list, zip(*current[::-1])))
        is_visited = [[False] * len(game_board[0]) for _ in range(len(game_board))]
        for i in range(N):
            for j in range(N):
                if current[i][j] >= 2 and not is_visited[i][j]:
                    g, b = make_table_group(i, j, current[i][j])
                    block[current[i][j]].append([b, g])

    # Grouping the GameBoard
    visited = [[False]*len(game_board[0]) for _ in range(len(game_board))]
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and not visited[i][j]:
                vacant, b = make_game_group(i, j)
                stop_flag = False

                for k, vals in block.items():
                    if stop_flag:
                        break
                    if not vals:
                        continue
                    for v in vals:
                        if vacant == v[1]:
                            for di, dj in vacant:
                                ni, nj = b[0]+di, b[1]+dj
                                game_board[ni][nj] = 1

                            for di, dj in v[1]:
                                ni, nj = v[0][0] + di, v[0][1] + dj
                                table[ni][nj] = 0
                                block[k] = []
                            ans += len(v[1])
                            stop_flag = True
                            break

    return ans


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]], 	[[1,1,1],[1,0,0],[0,0,0]]))