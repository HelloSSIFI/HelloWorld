from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    t = deque()
    for i in range(len(truck_weights)):                     # 각각 진입하는 트럭 순서대로 반복
        answer += 1                                         # 시간 1초 증가
        while sum(q) + truck_weights[i] > weight:           # 만약 다리에 진입할 수 없는 상태이면
            q.popleft()                                     # 다리에서 하나를 빼주고
            sec = t.popleft()                               # 현재시간과 다리를 지난 시간 중 큰 것을 가져옴
            answer = max(sec + bridge_length, answer)
        q.append(truck_weights[i])                          # 현재 트럭 무게와 시간을 각각 큐에 넣어줌
        t.append(answer)                                    # 마지막 트럭 진입 후 다리 길이만큼 지난 시간이 최종 정답
    return answer + bridge_length


# print(solution(2, 10, [7,4,5,6]))
