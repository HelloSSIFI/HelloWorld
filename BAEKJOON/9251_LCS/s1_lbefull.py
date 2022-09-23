A = input()
B = input()
N = len(A)
M = len(B)
dp = [0] * (N + 1)

for i in range(M):
    ndp = dp[:]
    for j in range(N):
        ndp[j + 1] = max(ndp[j + 1], ndp[j])
        if B[i] == A[j]:                                    # 현재 확인할 B의 문자열이 A의 문자열과 같다면
            ndp[j + 1] = max(ndp[j + 1], dp[j] + 1)         # 각각의 현재 문자열을 제외한 최대값에 1을 더한값과 비교하여 큰 값을 선택
    dp = ndp

print(dp[N])
