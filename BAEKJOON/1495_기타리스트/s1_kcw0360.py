N, S, M = map(int, input().split())    # N: 곡의 개수, S: 시작 볼륨, M: limit
vol = list(map(int, input().split()))    # 볼륨 리스트
dp = [[-1]*(M+1) for _ in range(N+1)]    # 각 곡마다 볼륨 크기(=idx)를 체크하기 위해 2차원 배열 생성
dp[0][S] = S    # 0번째 곡에 시작 볼륨 넣어주기

flag = True    # 볼륨 조절 할 수 있는지 체크
for i in range(N):    # 곡 순서대로 볼륨 조정
    for j in range(M+1):    # idx가 볼륨 크기 이기 때문에 i번째 곡에서 가질 수 있는 볼륨 찾기
        if dp[i][j] >= 0:    # 0 이상인 경우 i번째 곡에서 가질 수 있는 볼륨
            if dp[i][j] + vol[i] <= M:    # limit 값이 넘지 않는지 체크
                dp[i+1][dp[i][j] + vol[i]] = dp[i][j] + vol[i]    # 다음 곡 불륨 크기 저장
            if dp[i][j] - vol[i] >= 0:    # 0보다 작아지는지 체크
                dp[i + 1][dp[i][j] - vol[i]] = dp[i][j] - vol[i]

    if dp[i+1].count(-1) == M+1:    # 다음 곡에 저장 된 볼륨이 없다면 중간 볼륨 조절 할 수가 없는 경우
        flag = False
        break

if flag:
    print(max(dp[N]))
else:
    print(-1)

