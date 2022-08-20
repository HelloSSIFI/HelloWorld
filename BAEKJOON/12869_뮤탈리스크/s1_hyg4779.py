import sys

input = sys.stdin.readline

arr = []


def perm(cnt: object = int, now: object = list) -> object:
    if cnt == 3:
        arr.append(now)
        return
    tmp = [9, 3, 1]
    for i in range(3):
        if tmp[i] not in now:
            perm(cnt + 1, now + [tmp[i]])


perm(0, [])

n = int(input())
scv = list(map(int, input().split()))
if n < 3:
    scv += [0] * (3 - n)

dp = [[[-1] * 61 for _ in range(61)] for _ in range(61)]


def mutal(s: object=int, c: object=int, v: object=int) -> object:
    if s == 0 and c == 0 and v == 0:
        return 0

    def zero(n: object=int):
        return 0 if n < 0 else n

    if dp[s][c][v] != -1:
        return dp[s][c][v]

    dp[s][c][v] = 30
    for at in arr:
        dp[s][c][v] = min(dp[s][c][v], mutal(zero(s - at[0]), zero(c - at[1]), zero(v - at[2])))

    dp[s][c][v] += 1
    return dp[s][c][v]


print(mutal(scv[0], scv[1], scv[2]))
