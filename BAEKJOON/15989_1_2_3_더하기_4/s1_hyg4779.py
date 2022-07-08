T = int(input())
# 동전2 처럼 풀면 중복된 조합을 배제하지 못함
# 1로 만들 수 있는 모든 경우를 배열에 추가
dp = [1]*10001
# 2로 만들 수 있는 모든 경우를 배열에 추가
for i in range(2, 10001):
    dp[i] += dp[i-2]
# 3으로 만들 수 있는 모든 경우를 배열에 추가
for j in range(3, 10001):
    dp[j] += dp[j-3]

for _ in range(T):
    n = int(input())
    print(dp[n])