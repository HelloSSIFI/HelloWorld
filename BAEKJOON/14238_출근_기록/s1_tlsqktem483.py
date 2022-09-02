"""
5차원 dp + DFS
"""
import sys
input = sys.stdin.readline


def dfs(cnt_a, cnt_b, cnt_c, prev1, prev2):
    global dp

    if cnt_a < 0 or cnt_b < 0 or cnt_c < 0:
        return False

    if cnt_a == 0 and cnt_b == 0 and cnt_c == 0:
        return True

    if dp[cnt_a][cnt_b][cnt_c][prev1][prev2]:
        return False

    dp[cnt_a][cnt_b][cnt_c][prev1][prev2] = True
    ans[len(S)-(cnt_a+cnt_b+cnt_c)] = 'A'

    if dfs(cnt_a - 1, cnt_b, cnt_c, 0, prev1):
        return True

    if prev1 != 1:
        ans[len(S)-(cnt_a+cnt_b+cnt_c)] = 'B'
        if dfs(cnt_a, cnt_b - 1, cnt_c, 1, prev1):
            return True

    if prev1 != 2 and prev2 != 2:
        ans[len(S)-(cnt_a+cnt_b+cnt_c)] = 'C'
        if dfs(cnt_a, cnt_b, cnt_c - 1, 2, prev1):
            return True

    return False


S = list(input().rstrip())
C = {
    'A': 0,
    'B': 1,
    'C': 2
}
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
cnt = [S.count(c) for c in C.keys()]
ans = [''] * len(S)

if dfs(cnt[0], cnt[1], cnt[2], 0, 0):
    print(''.join(ans))
else:
    print(-1)
