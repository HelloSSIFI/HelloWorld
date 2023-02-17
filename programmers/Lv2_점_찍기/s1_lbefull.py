def solution(k, d):
    answer = 0
    y = 0
    for x in range(d, -1, -1):                  # x를 d, y를 0부터 시작해서
        while x ** 2 + y ** 2 <= d ** 2:        # 현재 y에서 거리 d 이내에있는 가장 큰 x값을 찾아
            answer += (x // k) + 1              # 해당 좌표까지 찍을 수 있는 점을 모두 더해줌
            y += k                              # y가 증가하면 최대 x값은 작아지므로 x는 그대로 두고 점점 줄여가며 탐색

    return answer


# print(solution(2, 4))
