import sys
input = sys.stdin.readline


T = int(input())

ans = []
for _ in range(T):
    K = int(input())
    chapter = list(map(int, input().split()))
    dp = [[0]*K for _ in range(K)]

    for i in range(1, K):
        for j in range(K-i):
            idx = i + j
            dp[j][idx] = 9876543210
            temp = sum(chapter[j:idx+1])
            for k in range(j, idx):
                dp[j][idx] = min(dp[j][idx], dp[j][k] + dp[k+1][idx] + temp)

    ans.append('{}\n'.format(dp[0][-1]))
print(''.join(ans))