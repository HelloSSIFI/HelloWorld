s, n = map(int, input().split())

result = [[] for _ in range(2*s+3)]
for num in str(n):
    board = [[' ']*(s+2) for _ in range(2*s+3)]    # 한칸 그릴 칸
    tmp = int(num)

    # 가로 - 상단 (0, 2, 3, 5, 6, 7, 8, 9)
    if tmp in [0, 2, 3, 5, 6, 7, 8, 9]:
        for i in range(1, s+1):
            board[0][i] = '-'

    # 세로 - 상단 (5, 6) (0, 4, 8, 9) (1, 2, 3, 7)
    # 좌상
    if tmp in [0, 4, 5, 6, 8, 9]:
        for i in range(1, s+1):
            board[i][0] = '|'
    # 우상
    if tmp in [0, 1, 2, 3, 4, 7, 8, 9]:
        for i in range(1, s+1):
            board[i][-1] = '|'

    # 가로 - 중단 (2, 3, 4, 5, 6, 8, 9)
    if tmp in [2, 3, 4, 5, 6, 8, 9]:
        for i in range(1, s+1):
            board[s+1][i] = '-'

    # 세로 - 하단 (2) (0, 6, 8) (1, 3, 4, 5, 7, 9)
    # 좌하
    if tmp in [0, 2, 6, 8]:
        for i in range(s+2, 2*s+2):
            board[i][0] = '|'
    # 우하
    if tmp in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        for i in range(s+2, 2*s+2):
            board[i][-1] = '|'

    # 가로 - 하단 (0, 2, 3, 5, 6, 8, 9)
    if tmp in [0, 2, 3, 5, 6, 8, 9]:
        for i in range(1, s+1):
            board[2*s+2][i] = '-'

    for i in range(2*s+3):
        result[i] += board[i] + [' ']

for ans in result:
    print(''.join(ans))