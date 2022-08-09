n = int(input())
train = [0] + list(map(int, input().split()))
pug = int(input())    # 소형 기관차가 최대로 끌 수 있는 객차 수
dp = [[0]*(n+1) for _ in range(4)]    # 1~3 까지 각 소형 기관차에 승객 수 누적

cnt = 1    # 소형 기관차 번호
while cnt < 4:    # 소형 기관차가 3개 이므로 3번까지 반복
    for i in range(cnt*pug, n+1):    # 열차(dp)에 저장시 이전 열차와 승객 수와 합산하여 누적해서 저장
        # 앞서 저장된 값과, 이전 열차의 dp값 + 현재 체크하는 소형 기관차의 승객수의 합 중 큰 값을 저장
        dp[cnt][i] = max(dp[cnt][i-1], dp[cnt-1][i-pug] + sum(train[i-pug+1:i+1]))
    cnt += 1    # 다음 열차로 진행

print(dp[3][n])





