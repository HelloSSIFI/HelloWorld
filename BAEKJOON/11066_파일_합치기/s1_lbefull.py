import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * K for _ in range(K)]                    # 합쳐진 파일 크기를 저장
    acc = [[0] * K for _ in range(K)]                   # 합쳐진 파일크기 + 현재까지 누적합을 저장
    for i in range(K):
        dp[i][i] = files[i]
    for i in range(1, K):                               # 대각선 방향으로 dp를 구해줌
        for j in range(K - i):                          # 인접한 장끼리 합
            min_v = 100000000                           # 합쳐질 장끼리 나올 수 있는 상황을 모두 파악해서
            for k in range(i + j, j, -1):               # 누적합이 가장 작은 것을 선택
                a = dp[k][i + j] + dp[j][k - 1]
                b = acc[k][i + j] + acc[j][k - 1]
                if a + b < min_v:
                    min_v = a + b
                    dp[j][i + j] = a
                    acc[j][i + j] = a + b
    result.append(str(acc[0][K - 1]))
print('\n'.join(result))
