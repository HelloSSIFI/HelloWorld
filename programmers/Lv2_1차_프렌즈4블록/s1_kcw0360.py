answer = 0
game = []

def block(m, n):
    global answer
    del_block = set()
    res = True

    dy = [0, 1, 1]
    dx = [1, 0, 1]

    for i in range(m-1):
        for j in range(n-1):
            temp = set()
            if game[i][j]:
                for k in range(3):
                    y = i + dy[k]
                    x = j + dx[k]

                    if game[i][j] == game[y][x]:
                        temp.add((y, x))
            if len(temp) == 3:
                temp.add((i, j))
                del_block |= temp

    if del_block:
        answer += len(del_block)
        for i in del_block:
            game[i[0]][i[1]] = 0

        for j in range(n):
            temp = []
            for i in range(m):
                if game[i][j]:
                    temp.append(game[i][j])
            length = m - len(temp)
            temp = ([0]*length) + temp
            for i in range(m):
                game[i][j] = temp[i]
    else:
        res = False

    return res

def solution(m, n, board):
    for i in board:
        game.append(list(i))

    while True:
        temp = block(m, n)
        if temp == False:
            break

    return answer

print(solution(6, 6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))