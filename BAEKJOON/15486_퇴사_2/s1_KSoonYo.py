import sys
input = sys.stdin.readline

N = int(input())
T = [0] * N               # 타임 테이블
P = [0] * N               # 가격 테이블
dp = [0] * (N + 1)        # dp 테이블, 마지막 날(N - 1번째)까지 최대 수익을 갱신 or 기록해야 하므로 N + 1 길이만큼 초기화

for i in range(N):
    t, p = map(int,input().split())
    T[i] = t
    P[i] = p

maxV = 0
for j in range(N):                                          # 상담을 하면 dp 테이블 갱신하고 i 증가, 하지 않는 경우 i 증가(maxV가 최대 수익을 계속 기억하고 있기 때문)
    maxV = max(maxV, dp[j])                                 # 지금까지의 기록에서 최대 수익을 갱신하면서 계속 기록해 둠
    
    if j + T[j] > N:
        continue
    
    dp[j + T[j]] = max(dp[j + T[j]], P[j] + maxV)

print(max(dp))
