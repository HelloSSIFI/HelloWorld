from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    progress = deque()                       # 다리를 지나는 중인 트럭

    t = 1
    now = 0
    while trucks or progress:
        # 다리에 트럭이 있는 경우
        if progress:
            if (t - progress[0][0]) >= bridge_length:
                passed = progress.popleft() 
                now -= passed[1]

            if trucks and now + trucks[0] <= weight:
                truck = trucks.popleft()
                progress.append((t, truck))
                now += truck

        # 다리에 트럭이 없는 상태지만 대기 트럭이 있는 경우
        elif trucks:
            truck = trucks.popleft()
            progress.append((t, truck))
            now += truck
        t += 1
    answer = t - 1

    return answer

