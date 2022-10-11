import sys
input = sys.stdin.readline


C, N = map(int, input().split())    # 홍보 고객 수, 홍보 도시 수

promotion = []
for _ in range(N):
    promotion.append(list(map(int, input().split())))   # [금액, 고객의 수]
promotion.sort()

# dp 생성(C 보다 더 많은 고객의 수가 비용이 적은 경우도 발생하며 주어진 값이 100보다 작거나 같기 때문에 99개 추가하여 확인)
dp = [0] + [10**5] * (C+99)

for cost, cnt in promotion:
    for idx in range(cnt, C+100):
        # dp[인원수] = min(dp[인원수], dp[인원수 - 고객수] + 비용)
        dp[idx] = min(dp[idx], dp[idx-cnt]+cost)

print(min(dp[C:]))  # C 고객수 이상에서 최소 비용 찾기