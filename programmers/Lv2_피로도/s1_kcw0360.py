from itertools import permutations


def solution(k, dungeons):
    answer = 0

    # (던전 순서)모든 경우 구해서 탐색한다.
    for fatigue in permutations(dungeons, len(dungeons)):
        now = k    # 현재 피로도
        res = 0    # 탐험한 던전 개수

        for condition in fatigue:    # 던전 탐험
            if now >= condition[0]:    # 들어갈 수 있는 던전
                now -= condition[1]    # 피로도 소모
                res += 1    # 탐험한 던전 개수 체크
            else:    # 못들어가는 경우 다음 순서는 탐험하지 않고 다른 경우의 수로 넘어간다.
                break

        answer = max(answer, res)    # answer와 res 중 큰 값을 저장

    return answer