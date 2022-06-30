import sys

N = int(input())
t, p = [], []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

M, dp = 0, [0]*(N+1)
for i in range(N):
    M = max(M, dp[i])                       # 현재 값 과 dp로 계산된 날짜의 값 중 최대값 갱신
    if i+t[i] > N:                          # 날짜가 지나면 continue
        continue
    dp[i+t[i]] = max(M+p[i], dp[i+t[i]])    # dp배열에 해당 상담날짜가 종료되는 날 값을
                                            # dp배열에 현재 최댓 값+상담 종료 후 금액 과
                                            # 현재까지의 상담 금액 + 현재 상담 종류후 금액중 최댓값으로 저장
print(max(dp))