from collections import deque


def solution(order):
    answer = 0
    stack = []
    convey = deque([i for i in range(1, len(order) + 1)])

    for i in range(len(order)):
        if stack and order[i] == stack[-1]:
            stack.pop()
            answer += 1
            continue

        flag = False
        while convey:
            m = convey.popleft()
            if order[i] == m:
                answer += 1
                flag = True
                break
            else:
                stack.append(m)
        if not flag:
            break
    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))