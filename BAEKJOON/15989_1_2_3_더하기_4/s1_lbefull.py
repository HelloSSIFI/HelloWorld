dp = [1] + [0] * 10000
for i in range(1, 4):                   # 동전 문제와 비슷하게
    for j in range(i, 10001):           # 1로 만들 수 있는 경우의 수에
        dp[j] += dp[j - i]              # 2를 추가했을 때 경우의 수를 더해주고 3도 마찬가지로 더해줌

for _ in range(int(input())):
    N = int(input())
    print(dp[N])
