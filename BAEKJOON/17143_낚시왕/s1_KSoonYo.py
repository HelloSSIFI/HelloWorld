# pypy3 통과

import sys
from collections import deque
input = sys.stdin.readline

def place(boards, sharks):
    while sharks:
        r, c, s, d, z  = sharks.popleft()
        if boards[r][c][4] < z:
            boards[r][c] = (r, c, s, d, z)

def fish(boards, fisher):
    for board in boards:
        if board[fisher][4]:
            z = board[fisher][4]
            board[fisher] = (board[fisher][0], board[fisher][1], 0, 0, 0)
            return z
    return 0


def search(boards, waiting):
    for board in boards:
        for i in range(len(board)):
            if board[i][4]:
                waiting.append(board[i])

def move(boards, R, C, dirs, turn, wait_sharks):
    sharks = deque()
    while wait_sharks:
        r, c, s, d, z = wait_sharks.popleft()
        boards[r][c] = (r, c, 0, 0, 0)

        k = 0
        while k < s:
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]            
            if 0 <= nr < R and 0 <= nc < C:
                r, c = nr, nc
                k += 1
            else:
                d = turn[d]
        sharks.append((r, c, s, d, z))
    place(boards, sharks)

R, C, M = map(int, input().split())
MAX_TIME = C
wait_sharks = deque()

dirs = [0, [-1, 0], [1, 0], [0, 1], [0, -1]]        # d의 방향값에 따른 방향 설정(상, 하, 우, 좌)

turn = {
    1 : 2, 2 : 1,                                   # 상 하 turn
    3 : 4, 4 : 3                                    # 좌 우 turn
}

boards = [[(i, j, 0, 0, 0) for j in range(C)]  for i in range(R)]     # (행 위치, 열 위치, 속력, 방향, 크기)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c- 1
    boards[r][c] = (r, c, s, d, z)

t = 0
total = 0
while t < MAX_TIME:
    total += fish(boards, t)
    search(boards, wait_sharks)
    move(boards, R, C, dirs, turn, wait_sharks)
    t += 1
print(total)

