# 현재 플레이어 입장에서 승리하면 True, 패배하면 False를 and turn + 1 과 함께 반환
def search(board, aloc, bloc, turn: int) -> (bool, int):
    # turn이 짝수면 A 차례, turn이 홀수면 B 차례
    r = aloc[0] if turn % 2 == 0 else bloc[0]
    c = aloc[1] if turn % 2 == 0 else bloc[1]

    # next location: 현재 차례 플레이어가 이동할 수 있는 다음 좌표
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    nloc = [[r + dy[d], c + dx[d]] for d in range(4)]
    nloc = [pos for pos in nloc
            if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]) and board[pos[0]][pos[1]] == 1]

    # 게임이 종료되는 경우
    if not nloc:    # 현재 진행하는 플레이어가 다음 좌표로 이동할 수 없는 경우 패배
        return False, 0
    elif aloc == bloc:    # 플레이어들의 위치가 같은 경우 다음 플레이어는 이동 불가하기 때문에 현재 플레이어의 승리
        return True, 1

    flag = False    # 현재 플레이어가 승리할 수 있는지 체크
    min_turn, max_turn = 25, 0

    # dfs
    for pos in nloc:
        board[r][c] = 0
        if turn % 2 == 0:
            result, cnt = search(board, pos, bloc, turn + 1)
        else:
            result, cnt = search(board, aloc, pos, turn + 1)
        board[r][c] = 1

        if not result:    # 다음 플레이어가 패배하는 경우 == 현재 플레이어가 승리하는 경우
            flag = True
            min_turn = min(min_turn, cnt + 1)
        elif not flag:
            max_turn = max(max_turn, cnt + 1)

    depth = min_turn if flag else max_turn

    return flag, depth


def solution(board, aloc, bloc):
    result, answer = search(board, aloc, bloc, 0)
    return answer