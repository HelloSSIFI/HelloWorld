def solution(weights):
    answer = 0
    w = [{}, {}, {}]                                                    # 2m, 3m, 4m 거리의 토크를 key, 개수를 value로 저장
    for weight in weights:
        for i in range(2, 5):                                           # weights의 원소들을 거리에 맞게 곱해서 딕셔너리에 저장
            w[i - 2][weight * i] = w[i - 2].get(weight * i, 0) + 1

    for cnt in w[2].values():                                           # 자신과 같은 몸무게가 있다면
        answer += cnt * (cnt - 1) // 2                                  # 총 n * (n - 1)의 짝이 지어지는데 자신이 포함된 것을 제외하면 2로 나누어지므로 해당 수를 더해줌

    for i in range(2):
        for j in range(i + 1, 3):                                       # 자신의 위치와 다른곳의 위치에 토크가 같은 사람을 찾아서
            for weight, cnt in w[i].items():                            # 해당 인원들로 짝을 지어 나올수 있는 조합(n * m)을 더해줌
                if weight in w[j]:
                    answer += cnt * w[j][weight]

    return answer


# print(solution([100, 180, 360, 100, 270]))
