N = int(input())

dp = [9876543210] * (N+1)
cannon_balls = []    # 사면체들이 가지고 있는 대포알 수 list
cnt = 0    # 한 사면체에 가지고 있는 대포알 수
idx = 1
while N > cnt:    # N까지 각 사면체가 가능한 대포알 수를 구한다.
    cnt += (idx * (idx+1)) // 2
    cannon_balls.append(cnt)
    idx += 1

for i in range(1, N+1):
    for j in cannon_balls:
        if i == j:    # 한 사면체로 만들 수 있는 경우
            dp[i] = 1
            break

        if i < j:    # 이전 사면체의 경우의 수와 비교를 위해 i-j를 했을때 0이하가 되면 안되기 때문에 체크
            break

        dp[i] = min(dp[i], dp[i-j] + 1)

print(dp[N])