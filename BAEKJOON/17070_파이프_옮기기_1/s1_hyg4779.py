import sys


def dfs(hr, hc, now):
    global res

    if hr == N-1 and hc == N-1:
        res += 1
        return

    if now != 1:                # 가로 이동 (가로, 대각)
        if hc+1 < N and arr[hr][hc+1] == 0:
            dfs(hr, hc+1, 0)

    if now != 0:                # 세로 이동 (세로, 대각)
        if hr+1 < N and arr[hr+1][hc] == 0:
            dfs(hr+1, hc, 1)


   # 대각 이동 (가로, 세로, 대각)
    if hr+1 < N and hc+1 < N:
        if arr[hr+1][hc+1] == 0 and arr[hr+1][hc] == 0 and arr[hr][hc+1] == 0:
            dfs(hr+1, hc+1, 2)


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = 0
dfs(0, 1, 0)

print(res)