import sys
input = sys.stdin.readline

dp = [1] * 10001                                    # 기본적으로 1은 모든 수를 표현할 수 있으므로 1개로 초기화

for i in range(2, 4):                               # 2를 추가할 때, 3을 추가할 때
    for j in range(i, 10001):                       # 10000 번째 dp 값까지 모두 채우기
        dp[j] += dp[j - i]

targets = []
for _ in range(int(input())):
    target = int(input())
    targets.append(target)

for num in targets:
    print(dp[num])



