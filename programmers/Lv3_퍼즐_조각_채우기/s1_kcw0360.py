import copy


def dfs(board, a, b, position, n, check):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    temp = [position]    # 블럭의 좌표를 더 해주기

    for k in range(4):
        y = a + dy[k]
        x = b + dx[k]

        if 0 <= y < n and 0 <= x < n and board[y][x] == check:
            board[y][x] = 2
            temp += dfs(board, y, x, [position[0] + dy[k], position[1] + dx[k]], n, check)

    return temp


def solution(game_board, table):
    answer = 0
    board = copy.deepcopy(game_board)

    n = len(board)
    block = []

    # 블럭(game_board의 빈칸)의 각 좌표 찾은 후 block에 추가
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                board[i][j] = 2    # 블럭 위치 표시
                block.append(dfs(board, i, j, [0, 0], n, 0)[1:])    # [0, 0] 뺀 블럭의 위치가 아닌 블럭에 대한 이동경로 탐색 위치를 저장

    # 90도씩 회전하면서 블록 확인
    for r in range(4):
        table = [list(i) for i in zip(*table[::-1])]    # 90도 회전
        table_rotate = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if table_rotate[i][j] == 1:    # table에서 블록인 경우
                    table_rotate[i][j] = 2    # 체크
                    tmp = dfs(table_rotate, i, j, [0, 0], n, 1)[1:]

                    if tmp in block:    # 블럭에 똑같은 경로를 이동하는 블럭이 있는지 확인
                        block.pop(block.index(tmp))    # 해당 블럭을 제거
                        answer += (len(tmp) + 1)    # 블럭 구성 칸 개수 = 이동경로 + 시작위치(1개)
                        table = copy.deepcopy(table_rotate)    # 사용된 블럭을 table에서 제거
                    else:
                        table_rotate = copy.deepcopy(table)    # 테이블 원상 복구

    return answer