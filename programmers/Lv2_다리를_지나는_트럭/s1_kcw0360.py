from collections import defaultdict, deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    check = defaultdict(int)    # 다리 위에서 차량이 지나 온 거리 체크
    for w in range(len(truck_weights)):
        check[w] = 0
    waiting = deque([num for num in range(len(truck_weights))])    # 대기중인 차량(먼저 출발하는 차량순서 대로 idx 설정)
    bridge = deque()    # 다리 위에 있는 차량 idx
    bridge_weights = deque()    # 다리 위에 있는 차량 무게

    while waiting or bridge:
        if bridge == []:    # 다리 위 차량이 없는 경우
            start = waiting.popleft()    # 출발
            bridge.append(start)
            bridge_weights.append(truck_weights[start])    # 다리 위 차량 무게 추가
            answer += 1    # 시간 경과
        else:
            # 다리 위 트럭들 무게 + 대기중인 트럭이 다리 제한 무게 초과한 경우
            if waiting:
                if sum(bridge_weights) + truck_weights[waiting[0]] > weight:
                    # 대기중인 트럭은 출발하지 않으며 첫 번째 트럭이 다리 위 가장 선두에 있는 트럭을 도착 시킨다.
                    com = bridge.popleft()
                    bridge_weights.popleft()
                    time = bridge_length - check[com]
                    answer += time    # 도착하는데 걸린 시간 추가

                    for idx in bridge:    # 다리 위 나머지 트럭 이동시간 추가
                        check[idx] += time
                else:
                    start = waiting.popleft()    # 대기중인 차량 출발
                    bridge.append(start)
                    bridge_weights.append(truck_weights[start])
                    answer += 1
                    for idx in bridge:    # 시간 경과
                        check[idx] += 1
                    if check[bridge[0]] == bridge_length:    # 도착한 트럭 제외
                        bridge.popleft()
                        bridge_weights.popleft()
            else:
                com = bridge.popleft()
                bridge_weights.popleft()
                time = bridge_length - check[com]
                answer += time

                for idx in bridge:
                    check[idx] += time

    return answer