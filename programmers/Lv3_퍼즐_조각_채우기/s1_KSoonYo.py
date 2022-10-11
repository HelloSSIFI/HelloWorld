from collections import deque


def get_puzzle(table_r, table_c, board, checked, start, status = 0):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    q = deque([start])
    result = [start]
    cnt = 1
    while q:
        r, c = q.popleft()
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < table_r and 0 <= nc < table_c and not checked[nr][nc]:
                if (status == 0 and board[nr][nc]) or (status and board[nr][nc] == 0):
                    cnt += 1
                    checked[nr][nc] = True
                    result.append((nr, nc))
                    q.append((nr, nc))
               
    return result, cnt

def make_cube(puzzle):
    maxR, maxC = 0, 0
    minR, minC = 51, 51
    for r, c in puzzle:
        maxR = max(maxR, r)
        maxC = max(maxC, c)
        minR = min(minR, r)
        minC = min(minC, c)
    
    R = maxR - minR + 1
    C = maxC - minC + 1

    puzzle = list(map(lambda x : (x[0] - minR, x[1] - minC), puzzle))

    # 정사각형 형태로 공백을 추가해서 늘리지 말고 딱 필요한 만큼의 가로, 세로 길이 큐브를 만들어야 함
    # 공백을 추가해서 억지로 정사각형 형태로 만들면, 공백 때문에 홈과 맞지 않는 경우 발생
    result = [[1] * C for _ in range(R)]
    for nr, nc in puzzle:
        result[nr][nc] = 0

    return result

def rotate(cube):
    result = [cube]
    for _ in range(3):
        cube = list(map(list, zip(*cube[::-1])))
        if cube not in result:
            result.append(cube)
    
    return result


def solution(game_board, table):
    answer = 0
    puzzles = {}

    # 퍼즐 추출
    table_r = len(table)
    table_c = len(table[0])
    checked = [[False] * table_c for _ in range(table_r)]
    puzzle_idx = 0
    for i in range(table_r):
        for j in range(table_c):
            if table[i][j] and not checked[i][j]:
                checked[i][j] = True
                puzzles[puzzle_idx] = []
                puzzle, cnt = get_puzzle(table_r, table_c, table, checked, start=(i, j))
                cube = make_cube(puzzle)

                # 큐브를 회전해서 도출할 수 있는 모든 경우 저장
                puzzles[puzzle_idx] = rotate(cube)
        
                puzzle_idx += 1

    # 홈 추출
    new_checked = [[False] * table_c for _ in range(table_r)]
    used = [False] * (50 ** 2 + 1)
    for r in range(table_r):
        for c in range(table_c):
            if game_board[r][c] == 0 and not new_checked[r][c]:
                new_checked[r][c] = True
                slots, cnt = get_puzzle(table_r, table_c, game_board, new_checked, start=(r, c), status=1)
                slots_cube = make_cube(slots)

                # 끼워 맞추기
                for idx in puzzles.keys():
                    if slots_cube in puzzles[idx] and not used[idx]:
                        used[idx] = True
                        answer += cnt
                        break
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
