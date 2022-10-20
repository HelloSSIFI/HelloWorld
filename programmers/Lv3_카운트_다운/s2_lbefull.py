def solution(target):
    score_set = set([50])                                   # 한 번 던져서 얻을 수 있는 점수를 모두 담아줌
    for i in range(1, 21):
        for j in range(1, 4):
            score_set.add(i * j)

    dp = [[1, 0] if i in score_set else [200000, 0] for i in range(100001)]
    for i in range(1, 21):                                  # dp의 인덱스를 점수로하여 던진횟수와 싱글,불 횟수를 저장
        dp[i][1] = 1                                        # 초기 1~60 까지의 점수 중
    dp[50][1] = 1                                           # 싱글과 불의 점수에 해당한다면 dp의 두번째 값을 1로 바꿔줌

    for i in range(21, 61):                                 # dp의 1~60 까지의 점수를 초기화 하기위해
        if dp[i] != [200000, 0]:                            # score_set에 있는 점수는 횟수를 1로 설정하고
            continue                                        # 그 이외의 점수들은 횟수와 싱글,불 횟수를 구해줌

        dp[i][0] = 2                                        # 기본적으로 1~60 사이의 점수는 최소횟수가 2를 넘기지 않음
        for s in score_set:                                 # score_set을 순회하면서 현재 회차에 올릴 점수를 가져옴
            if i - s <= 0 or dp[i - s][0] != 1:             # 점수가 마이너스로 가거나 횟수가 2인곳에서 한번 더 던져 3을 만들필요는 없으므로
                continue                                    # 이런 경우는 다음반복

            n = dp[i - s][1]                                # 현재 회차의 점수가 싱글과 불이라면
            if s < 21 or s == 50:                           # dp의 이전값과 더해서 n으로 구해줌
                n += 1

            dp[i][1] = max(dp[i][1], n)                     # 더 큰 값을 선택

    for i in range(61, target + 1):                         # 61점 이상부터 dp를 계속 구해줌
        for s in score_set:                                 # 한번 던져 나올 수 있는 점수를 모두 순회
            n = dp[i - s][1]                                # 싱글, 불 여부에 따라 n값을 구해주고
            if s < 21 or s == 50:
                n += 1

            if dp[i - s][0] + 1 < dp[i][0]:                 # 현재 점수대로 던졌을 때 횟수가 더 적다면
                dp[i][0] = dp[i - s][0] + 1                 # 횟수와 싱글, 불을 모두 갱신하고
                dp[i][1] = n

            elif dp[i - s][0] + 1 == dp[i][0]:              # 횟수가 같지만, 싱글, 불이 클 경우
                dp[i][1] = max(dp[i][1], n)                 # 싱글, 불만 갱신

    return dp[target]
