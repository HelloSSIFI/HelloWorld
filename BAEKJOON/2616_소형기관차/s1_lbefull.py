N = int(input())
num = [0] + list(map(int, input().split()))
M = int(input())
dp = [[0, 0, 0, 0] for _ in range(N + 1)]                       # 각각 소형기관차가 1대, 2대, 3대일 때 최대 승객을 저장

temp = sum(num[:M])
for i in range(M, N + 1):                                       # M번 객차부터 순회
    temp += num[i]                                              # 현재 객차를 포함해 이전 M개의 수를 temp에 저장
    temp -= num[i - M]                                          # 현재 객차를 선택하고 객차가 한 대적을 때 최대값을 더해준 값과
    for j in range(1, 4):                                       # 이전 최대값을 비교해 큰 값을 선택
        dp[i][j] = max(dp[i - 1][j], temp + dp[i - M][j - 1])

print(dp[-1][-1])
