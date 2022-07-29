# pypy3 통과
import sys

input = sys.stdin.readline


def move_pipe(status, start, end):
    global cnt
    if start == end:
        cnt += 1
        return

    if status != 'c':
        if 0 < start[0] <= N and 0 < start[1] + 1 <= N and graph[start[0]][start[1] + 1] == 0:
            move_pipe('r', (start[0], start[1] + 1), end)

    if status != 'r':
        if 0 < start[0] + 1 <= N and 0 < start[1] <= N and graph[start[0] + 1][start[1]] == 0:
            move_pipe('c', (start[0] + 1, start[1]), end)
    
    if 0 < start[0] + 1 <= N and 0 < start[1] + 1 <= N and graph[start[0] + 1][start[1] + 1] == 0:
        if graph[start[0] + 1][start[1]] == 0 and graph[start[0]][start[1] + 1] == 0:
            move_pipe('cr', (start[0] + 1, start[1] + 1), end)

N = int(input())
graph = [[-1] * (N + 1)] + [[-1] + list(map(int, input().split()))  for _ in range(N)]
cnt = 0
move_pipe('r', (1, 2), (N, N))
print(cnt)

'''
# fail
# 시간 초과
import sys

input = sys.stdin.readline


def move_pipe(status, start, end, next_direction = []):
    global cnt
    if start == end:
        cnt += 1
        return

    if status == 'r':
        next_direction = dr
    elif status == 'c':
        next_direction = dc
    else:
        next_direction = dcr

    for next in next_direction:
        nr, nc = next_table[next](start[0], start[1])
        if 0 < nr <= N and 0 < nc <= N:
            if (next != 'cr' and graph[nr][nc] == 0) or (next == 'cr' and (graph[nr][nc], graph[nr - 1][nc], graph[nr][nc - 1]) == (0, 0, 0)):
                move_pipe(next, (nr, nc), end)


N = int(input())
graph = [[-1] * (N + 1)] + [[-1] + list(map(int, input().split()))  for _ in range(N)]
next_table = {
    'cr' : lambda x, y : (x + 1, y + 1),
    'r' :  lambda x, y : (x, y + 1),
    'c' : lambda x, y : (x + 1, y)
}

dcr = ['cr', 'r', 'c']
dr = ['cr', 'r']
dc = ['cr', 'c']

cnt = 0
move_pipe('r', (1, 2), (N, N))
print(cnt)
'''
