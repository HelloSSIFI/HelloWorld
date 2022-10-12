import sys
from collections import deque
input = sys.stdin.readline


def spring_summer():
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] <= nu[i][j]:
                    nu[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, len(tree[i][j])):
                        nu[i][j] += tree[i][j].pop()//2
                    break


def fall_winter():
    for i in range(N):
        for j in range(N):
            for k in tree[i][j]:
                if k % 5 == 0:
                    for di in d:
                        ni, nj = i + di[0], j + di[1]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree[ni][nj].appendleft(1)
            nu[i][j] += a[i][j]


N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
d = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
nu = [[5]*N for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    x, y = x-1, y-1
    tree[x][y].append(age)

for _ in range(K):
    spring_summer()
    fall_winter()

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(tree[i][j])
print(cnt)