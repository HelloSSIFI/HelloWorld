def solution(order):
    answer = 0
    stack = []
    idx = 0

    for i in range(1, len(order)+1):
        if order[idx] == i:
            answer += 1
            idx += 1
            while stack:
                if stack[-1] == order[idx]:
                    answer += 1
                    idx += 1
                    stack.pop()
                else:
                    break
        else:
            while stack:
                if stack[-1] == order[idx]:
                    answer += 1
                    idx += 1
                    stack.pop()
                else:
                    break
            stack.append(i)


    return answer