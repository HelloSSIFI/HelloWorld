def solution(order):
    answer = 0
    stack = []
    i = 1
    for main in range(len(order)):

        if order[main] < i:
            if stack and stack[-1] == order[main]:
                stack.pop()
                answer += 1

            elif stack and stack[-1] != order[main]:
                break
        else:
            while i <= order[main]:
                if i < order[main]:
                    stack.append(i)
                i += 1
            answer += 1

    return answer