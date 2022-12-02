import sys
input = sys.stdin.readline



dp = [[0] * 10 for _ in range(65)]              # n자리수(최대 64)와 각 자리수에서 0~9로 이루어진 64 x 10 dp를 만듬
for i in range(10):                             # 각 자리수에는 0~9로 시작하는 숫자가 몇개인지 저장
    dp[1][i] = 1

for i in range(2, 65):                          # n자리 수에서 0으로 시작하는 수는 n - 1 자리수 숫자 모두를 포함할 수 있고
    temp = sum(dp[i - 1])                       # n자리 수에서 1로 시작하는 수는 n - 1 자리 숫자 중
    for j in range(10):                         # 0으로 시작하는 수를 제외한 수를 포함할 수 있음
        dp[i][j] = temp                         # 마찬가지로 2, 3... 을 계속 구해서 dp에 저장
        temp -= dp[i - 1][j]

answer = []
for _ in range(int(input())):
    answer.append(sum(dp[int(input())]))

print(*answer, sep='\n')
