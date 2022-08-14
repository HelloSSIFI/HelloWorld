import sys
input = sys.stdin.readline
N, M = map(int, input().split())

A = list(map(int, input().split()))
C = list(map(int, input().split()))

total = sum(C)
result = sys.maxsize

# dp[i][j] = i번째 앱까지 비용 j로 얻을 수 있는 최대 메모리
dp = [[0 for _ in range(total+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(total):
        # C[i]가 비용 j를 넘어가면 종료시킬 수 없으므로 이전 값을 그대로 가져온다
        if C[i] > j:
            dp[i][j] = dp[i-1][j]
        # C[i]가 비용 j보다 작거나 같으면 종료 시킬 수 있다.
        # 앱을 종료시키지 않았을 떄, 종료시켰을 때 가질 수 있는 최댓값을 비교
        else:
            dp[i][j] = max(dp[i-1][j], A[i]+dp[i-1][j-C[i]])

        if dp[i][j]>=M:
            result = min(result, j)

if M==0:
    print(0)
    exit()
elif N==1:
    print(C[0])
elif result == sys.maxsize:
    print(N*M)
else:
    print(result)