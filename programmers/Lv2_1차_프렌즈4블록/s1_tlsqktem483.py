def arrange(m, n, game_map):
    temp = [['']*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = game_map[j][i]
    for r in range(n):
        flag = False
        for c in range(m):
            if temp[r][c] != '0':
                flag = True
            if flag and temp[r][c] == '0':
                temp[r].pop(c)
                temp[r].insert(0, '0')
    for i in range(m):
        for j in range(n):
            game_map[i][j] = temp[j][i]
    return game_map


def check(r, c, game_map):
    if game_map[r][c] != '0' and game_map[r][c+1] == game_map[r][c] and game_map[r+1][c] == game_map[r][c] and game_map[r+1][c+1] == game_map[r][c]:
        return True
    else:
        return False


def game(m, n, game_map, cnt):
    boom = [item[:] for item in game_map]
    di = [(0, 0), (0, 1), (1, 0), (1, 1)]
    flag = False
    for i in range(m-1):
        for j in range(n-1):
            if check(i, j, game_map):
                flag = True
                for d in di:
                    r, c = i + d[0], j + d[1]
                    if boom[r][c] != '0':
                        boom[r][c] = '0'
                        cnt += 1

    # print(cnt, flag)
    if not flag:
        return cnt
    game_map = arrange(m, n, boom)
    return game(m, n, game_map, cnt)


def solution(m, n, board):
    game_map = [[]*n for _ in range(m)]
    for i in range(m):
        game_map[i] = list(board[i])
    answer = game(m, n, game_map, 0)
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))