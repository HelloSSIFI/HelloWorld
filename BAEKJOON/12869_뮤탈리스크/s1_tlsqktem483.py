import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
hp = list(map(int, input().split()))
dp = [[[100 for _ in range(61)] for _ in range(61)] for _ in range(61)]
ans = 100

while len(hp) < 3:
    hp.append(0)


def dfs(x, y, z, cnt):
    global ans
    if x <= 0 and y <= 0 and z <= 0:
        if ans > cnt:
            ans = cnt
            return

    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return

    dp[x][y][z] = cnt

    for i in permutations([9, 3, 1], 3):
        dfs(x - i[0], y - i[1], z - i[2], cnt + 1)


dfs(hp[0], hp[1], hp[2], 0)
print(ans)
