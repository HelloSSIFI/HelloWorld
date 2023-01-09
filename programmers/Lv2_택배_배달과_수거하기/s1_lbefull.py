def solution(cap, n, deliveries, pickups):
    answer = d = p = cnt = 0
    i = j = n
    while 0 <= i or 0 <= j:                     # 배달과 수거를 모두 마칠때까지 반복
        while d <= cap * cnt:                   # 배달 먼저 체크
            i -= 1                              # cap개의 택배를 가장 먼 집부터 배달
            if i < 0: break
            d += deliveries[i]

        while p <= cap * cnt:                   # cap개의 빈 상자를 먼 집부터 수거
            j -= 1
            if j < 0: break
            p += pickups[j]

        answer += (max(i, j) + 1) * 2           # 남은 배달과 수거 중 가장 더 먼거리를 이동해야 하므로 answer에 왕복 거리를 추가
        cnt += 1                                # 회차 +1

    return answer


# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
