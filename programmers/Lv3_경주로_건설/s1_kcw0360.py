from collections import deque


def solution(board):
    answer = 9876543210
    n = len(board)
    dp = [[9876543210]*n for _ in range(n)]
    directions = {0: [-1, 0], 1: [1, 0], 2: [0, -1], 3: [0, 1]}
    q = deque([[0, 0, 0, -1]])

    while q:
        a, b, res, direction = q.popleft()

        if [a, b] == [n-1, n-1] and answer > res:
            answer = res

        for d in range(4):
            y, x = a + directions[d][0], b + directions[d][1]

            if direction == d or direction == -1:
                add = 100
            else:
                add = 600

            if 0 <= y < n and 0 <= x < n and board[y][x] != 1 and dp[y][x] >= res + add - 400:
                dp[y][x] = res + add
                q.append([y, x, res+add, d])

    return answer