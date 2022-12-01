def solution(k, ranges):
    answer = []
    y = [k]
    while y[-1] != 1:                                   # 우박수열의 진행단계에 따른 값을 y리스트에 저장
        if y[-1] % 2:
            y.append(y[-1] * 3 + 1)
        else:
            y.append(y[-1] // 2)

    N = len(y)
    acc = [0]                                           # 위에서 구한 y값을 이용하여 0 ~ i(=x) 까지 넓이를 acc[i]에 저장
    for i in range(1, N):
        acc.append(acc[-1] + min(y[i], y[i - 1]) + abs(y[i] - y[i - 1]) / 2)

    for x1, x2 in ranges:
        x2 = N + x2 - 1                                 # 문제에서 주어진 범위를 x축 값으로 변환
        if x1 > x2:                                     # 시작 좌표가 끝 좌표보다 크면 -1
            answer.append(-1)
            continue
        answer.append(acc[x2] - acc[x1])                # 아니라면 해당 범위 면적을 answer에 추가
    return answer


# print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
