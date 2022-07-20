from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])

    while len(queue):
        current = queue.popleft()

        if queue and max(queue)[0] > current[0]:
            queue.append(current)
        else:
            answer += 1

            if current[1] == location:
                break
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))