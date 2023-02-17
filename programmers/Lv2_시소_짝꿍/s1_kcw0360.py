from collections import Counter


def solution(weights):
    answer = 0
    info = Counter(weights)    # 몸무게: 사람수
    check = [3/2, 2, 4/3]    # 거리에 따른 비율

    for weight in info:
        if info[weight] >= 2:    # 같은 몸무게인 사람들끼리 짝을 만들때 나오는 경우의 수
            answer += (info[weight] - 1) * info[weight] // 2

        for i in check:
            temp = weight * i
            if temp in info:    # 시소가 균형을 이루는 경우
                answer += info[weight] * info[temp]    # 몸무게 해당하는 사람들 끼리 짝을 만들때 나오는 경우의 수 추가

    return answer