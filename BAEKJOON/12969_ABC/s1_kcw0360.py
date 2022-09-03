N, K, = map(int, input().split())    # N: 문자열 길이, K: 쌍의 개수
# dp[i][a][b][p] = dp[문자열 길이][A의 개수][B의 개수][페어 수] - 페어(A,B)(A,C)(B,C)
dp = [[[[0 for _ in range(N(N-1)//2)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
ans = [0] * N


def check(i, a, b, p):
    if i == N:    # 문자열이 완성된 경우
        if p == K:    # 쌍의 개수가 만족했을 경우
            return 1
        return 0

    if dp[i][a][b][p]:    # 중복 방지
        return 0

    dp[i][a][b][p] = 1    # 방문 체크

    ans[i] = 'A'
    if check(i+1, a+1, b, p):
        return 1

    ans[i] = 'B'
    if check(i+1, a, b+1, p+a):
        return 1

    ans[i] = 'C'
    if check(i+1, a, b, p+a+b):
        return 1
    return 0


if check(0, 0, 0, 0):
    print(''.join(ans))
else:
    print(-1)
