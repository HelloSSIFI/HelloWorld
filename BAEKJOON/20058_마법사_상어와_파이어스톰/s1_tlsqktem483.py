"""
얼음 녹는 시점 조심
"""
from collections import deque


def bfs(r, c):
    global visited
    q = deque()
    q.append([r, c])
    cnt = 0

    while q:
        i, j = q.popleft()

        for di in d:
            ni, nj = i + di[0], j + di[1]
            if 0 <= ni < 2**N and 0 <= nj < 2**N and a[ni][nj] and not visited[ni][nj]:
                q.append([ni, nj])
                cnt += 1
                visited[ni][nj] = True

    return cnt


def rotation(l):
    global a
    pointer = 2**l

    for i in range(2**N):
        for j in range(2**N):
            if i % pointer == 0 and j % pointer == 0:
                temp = []
                for r in range(i, i+pointer):
                    temp.append(a[r][j:j+pointer])
                arr = list(map(list, zip(*temp[::-1])))
                for r in range(i, i+pointer):
                    a[r][j:j+pointer] = arr[r % pointer][:]


N, Q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for l in L:
    rotation(l)
    check_list = []
    for i in range(2**N):
        for j in range(2**N):
            if not a[i][j]:
                continue
            cnt = 0
            for di in d:
                ni, nj = i + di[0], j + di[1]
                if 0 <= ni < 2**N and 0 <= nj < 2**N and a[ni][nj]:
                    cnt += 1
            if cnt < 3:
                check_list.append([i, j])
    # Melting
    for r, c in check_list:
        a[r][c] -= 1
sum_v = 0
cnt = 0
visited = [[False]*(2**N) for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if a[i][j]:
            sum_v += a[i][j]
            if not visited[i][j]:
                cnt = max(cnt, bfs(i, j))

print(sum_v)
print(cnt)
