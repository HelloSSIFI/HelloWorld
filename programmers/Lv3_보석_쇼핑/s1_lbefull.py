def solution(gems):
    N = len(gems)
    M = len(set(gems))
    answer = [0, N]
    buys = dict()
    s = e = 0
    while s < N:
        if len(buys) == M and s <= e:                           # 만약 e가 모든 보석을 살 수 있을때까지 전진했으면
            while len(buys) == M and s <= e:                    # s도 모든 보석을 살 수있는 구간에서 최대한 전진
                buys[gems[s]] -= 1
                if buys[gems[s]] == 0:
                    buys.pop(gems[s])
                s += 1
            if answer[1] - answer[0] > e - s:                   # e와 s 구간이 저장된 구간보다 짧다면 갱신
                answer = [s, e]
        else:                                                   # 모든 보석을 살 수 없다면 e를 전진
            if e == N:                                          # 만약 e가 N이라면 반복종료
                break
            while e < N and len(buys) < M:                      # 범위 내에서 모든 보석을 살 수 있을때까지 전진
                buys[gems[e]] = buys.get(gems[e], 0) + 1
                e += 1
    return answer


# print(solution(["XYZ", "XYZ", "XYZ"]))
