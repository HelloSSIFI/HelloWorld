def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries and deliveries[-1] == 0:
        deliveries.pop()

    while pickups and pickups[-1] == 0:
        pickups.pop()

    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2

        box = 0
        while box <= cap and deliveries:
            if deliveries[-1] + box <= cap:
                box += deliveries.pop()
            else:
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