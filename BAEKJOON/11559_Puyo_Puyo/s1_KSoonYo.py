import sys
from collections import deque
input = sys.stdin.readline

def puyo(game, visited, start):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([start])
    game[start[0]][start[1]] = '.'
    while q:
        r, c = q.popleft()
        for m in range(4):
            nr = r + dr[m]
            nc = c + dc[m]
            if 0 <= nr < 12 and 0 <= nc < 6 and visited[nr][nc]:
                if game[nr][nc] != '.':
                    game[nr][nc] = '.'
                    q.append((nr, nc))

game_map = [list(input().strip()) for _ in range(12)]

# bfs
q = deque([(1, game_map)])                     # (puyo n회차, puyo 이후 게임 맵)
bomb = 0

while q:
    n, game_map = q.popleft()
    
    is_puyo = False
    for i in range(11, -1, -1):
        if game_map[i].count('.') == 6:
            continue

        for j in range(6):
            if game_map[i][j] == '.':
                continue
            puyo_color = game_map[i][j]

            visited = [[False] * 6 for _ in range(12)]
            
            blocks = deque([(i, j)])
            visited[i][j] = True

            cnt = 1    
            dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

            while blocks:
                r, c = blocks.popleft()
                
                for m in range(4):
                    nr = r + dr[m]
                    nc = c + dc[m]
                    if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and game_map[nr][nc] == puyo_color:
                        cnt += 1
                        visited[nr][nc] = True
                        blocks.append((nr, nc))

            # puyo
            if cnt >= 4:
                puyo(game_map, visited, start=(i, j))
                is_puyo = True
    
    if not is_puyo:
        continue

    bomb += 1
    # after puyo map(swap)
    for i in range(11, -1, -1):
        for j in range(6):
            if game_map[i][j] == '.':
                pointer1, pointer2 = i, i - 1
                while pointer2 >= 0:
                    if game_map[pointer2][j] != '.':
                        game_map[pointer1][j], game_map[pointer2][j] = game_map[pointer2][j], game_map[pointer1][j]
                        pointer1 -= 1
                    pointer2 -= 1

    # next queue push
    q.append((n + 1, game_map))
print(bomb)