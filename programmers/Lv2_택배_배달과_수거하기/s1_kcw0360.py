def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries and deliveries[-1] == 0:    # 가장 먼 집부터 차례로 체크하며 배달해야할 첫 집 찾기
        deliveries.pop()

    while pickups and pickups[-1] == 0:    # 가장 먼 집부터 차례로 체크하며 수거해야할 첫 집 찾기
        pickups.pop()

    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2    # 둘 중 먼 곳 집의 거리를 answer에 추가(왕복거리라 *2)

        box = 0    # 현재 박스 수
        while box <= cap and deliveries:
            if deliveries[-1] + box <= cap:    # 트럭에 실을 수 있는 최대치 보다 적은 경우
                box += deliveries.pop()
            else:    # 최대치 보다 많은 경우
                deliveries[-1] -= cap-box
                break

        box = 0
        while box <= cap and pickups:
            if pickups[-1] + box <= cap:
                box += pickups.pop()
            else:
                pickups[-1] -= cap-box
                break

    return answer