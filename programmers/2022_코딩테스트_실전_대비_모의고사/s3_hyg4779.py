def solution(order):
    answer = 1

    N = len(order)
    Q = [0]*(N+1)
    for i in range(1, N+1):
        Q[order[i-1]] = i

    stack = [0]*(N+1)

    idx, top = 1, -1

    while answer <= N:
        if stack[top] == answer:
            top -= 1
            answer += 1
        elif Q[idx] == answer:
            idx += 1
            answer += 1
        else:
            if idx == N:
                break
            else:
                top += 1
                stack[top] = Q[idx]
                idx += 1

    return answer-1
