import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if lines[j][k] > lines[j][i] + lines[i][k]:
                lines[j][k] = lines[j][i] + lines[i][k]

for i in range(M):
    A, B, C = map(int, input().split())
    if lines[A - 1][B - 1] > C:
        print('Stay here')
    else:
        print('Enjoy other party')
