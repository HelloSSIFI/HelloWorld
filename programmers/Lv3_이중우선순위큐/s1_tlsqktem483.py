from collections import deque


def solution(operations):
    queue = deque()

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == 'I':
            queue.append(num)
        elif num < 0 and queue:
            queue.remove(min(queue))
        elif num > 0 and queue:
            queue.remove(max(queue))

    return [max(queue), min(queue)] if queue else [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))