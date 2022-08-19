from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
answer = 0
q = deque()

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            q.append([i, j])

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

while q:
    a, b = q.popleft()

    for k in range(8):
        i = a + dy[k]
        j = b + dx[k]

        if 0 <= i < N and 0 <= j < M and space[i][j] == 0:
            space[i][j] = space[a][b] + 1
            q.append([i, j])

for i in range(N):
    answer = max(answer, max(space[i]))

print(answer-1)