from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

def isCompleted(N, labs, checked):
    for i in range(N):
        for j in range(N):
            if labs[i][j] == 0 and checked[i][j] == float('inf'):
                return False
    return True

def spread(N, labs, checked, case):
    global min_time

    q = deque([*case])
    times = set()
    times.add(0)
    while q:
        r, c = q.popleft()
        
        # if checked[r][c] > min_time:
        #     return

        if labs[r][c] != 2:
            times.add(checked[r][c])

        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < N and labs[nr][nc] != 1 and checked[nr][nc] > checked[r][c] + 1:
                checked[nr][nc] = checked[r][c] + 1
                q.append((nr, nc))
    
    if isCompleted(N, labs, checked) and min_time > max(times):
        min_time = max(times)


N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]
viruses = set()

for i in range(N):
    for j in range(N):
        if labs[i][j] == 2:
            viruses.add((i, j))

min_time = float('inf')

origin = [[float('inf')] * N for _ in range(N)]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for case in combinations(viruses, M): 
    checked = [i[:] for i in origin]
    for virus in case:
        r, c = virus
        checked[r][c] = 0
    spread(N, labs, checked, case)

print(min_time if min_time != float('inf') else -1)
