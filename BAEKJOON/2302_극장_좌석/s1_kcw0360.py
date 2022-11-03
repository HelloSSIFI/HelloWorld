import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]    # 고정석
dp = [0] * (N+1)
dp[1] = 1    # 자리가 1가지일 때 앉을 수 있는 경우의 수
dp[0] = 1    # default

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]    # 점화식

check = 0    # 고정석 체크
answer = 1    # 좌석의 수는 최소 1자리 이상이므로 초기값 1로 시작
for i in vip:
    temp = i - 1 - check    # 고정석 번호까지 고정석이 아닌 좌석의 수
    answer *= dp[temp]    # dp에서 해당 좌석 수가 만들어 내는 경우의 수를 answer에 곱
    check = i    # 고정석 위치 변경
answer *= dp[N-check]    # 마지막 고정석 부터 나머지 좌석 까지의 경우도 계산

print(answer)