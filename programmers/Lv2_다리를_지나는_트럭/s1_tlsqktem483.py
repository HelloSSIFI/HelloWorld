"""
Key : bridge 배열을 시간별로 update
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    ans = 0
    trucks = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    w_sum = 0
    while bridge:
        ans += 1
        w_sum -= bridge.popleft()

        if trucks:
            if w_sum + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                w_sum += truck
            else:
                bridge.append(0)

    return ans


print(solution(2, 10, 	[7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, 	[10,10,10,10,10,10,10,10,10,10]))