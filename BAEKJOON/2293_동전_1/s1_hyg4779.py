N, K = map(int, input().split())        # N개의 동전 종류, 목표값 K
coins = [int(input()) for _ in range(N)]
'''
DP 문제 풀이 핵심: 전체의 문제를 부분 문제로 나누기 > 점화식 세우기 > 부분 문제 사이에 모든 관계를 고려하기
https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2293-%EB%8F%99%EC%A0%84-1 : 나동빈 DP 
'''
dp = [0]*(K+1)
dp[0] = 1

for i in coins:
    for j in range(i, K+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[K])

