import sys
input = sys.stdin.readline


def dfs(i, a, b, cnt):
    global ans
    if i == N:
        if cnt == K:
            return True
        else:
            return False

    if dp[i][a][b][cnt]:
        return False
    dp[i][a][b][cnt] = True

    ans[i] = 'A'
    if dfs(i + 1, a + 1, b, cnt):
        return True

    # B 가 추가되면 A 갯수만큼 pair 증가
    ans[i] = 'B'
    if dfs(i + 1, a, b + 1, cnt + a):
        return True

    # C 가 추가되면 A, B 갯수만큼 pair 증가
    ans[i] = 'C'
    if dfs(i + 1, a, b, cnt + a + b):
        return True

    return False


N, K = map(int, input().split())

dp = [[[[0 for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)]
ans = [''] * N
if dfs(0, 0, 0, 0):
    print(''.join(ans))
else:
    print(-1)