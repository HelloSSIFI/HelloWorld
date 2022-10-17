def solution(target):
    arr = [[i for i in range(1, 21)], []]    # [[single, bull로 만들 수 있는 점수], [single, bull로 만들 수 없는 점수]]
    arr[0].append(50)
    temp = set()
    for i in range(1, 21):
        for j in range(2, 4):
            tmp = i * j
            if tmp > 20:    # single로 만들 수 있는 수 제외
                temp.add(tmp)
    arr[1] = list(temp)

    dp = [[100000, 0] for _ in range(target + 1)]    # [최소 다트 수, single+bull]
    dp[0][0] = 0

    for i in range(1, target + 1):
        for j in range(2):    # arr의 idx
            for k in range(len(arr[j])):    # 다트를 한번 던졌을 때 만들 수 있는 모든 경우의 수로 체크
                prev = i - arr[j][k]    # 이전 값 체크를 위한 idx

                if prev < 0:    # 0 이하의 수는 skip
                    continue

                # tot: 이전 값에서 다트 수 +1, valid: single, bull을 사용한 list를 체크하고 있다면 +1 아니면 +0
                tot, val = dp[prev][0] + 1, dp[prev][1] + 1 - j

                if tot < dp[i][0]:    # tot값이 현 위치의 값보다 작은 경우 dp[i] 값 갱신(val도 바뀔 수 있다)
                    dp[i] = [tot, val]
                elif tot == dp[i][0]:    # tot값이 같은 경우엔 single or bull 사용 횟수가 많은 것으로 갱신
                    dp[i][1] = max(dp[i][1], val)

    return dp[target]