def solution(order):
    answer = 0
    N = len(order)
    orders = [0] * N
    stack = []
    for i in range(N):
        orders[N - order[i]] = i                            # 상자 순서를 재정의

    while orders or stack:                                  # 상자가 남아있는 동안 반복
        if stack and answer == stack[-1]:                   # 보조 컨테이너 벨트를 확인하여 현재 실어야 할 순서라면 실어줌
            answer += 1
            stack.pop()
            continue

        while orders and orders[-1] != answer:              # 위 경우가 아니라면 택배 순서를 확인하여
            stack.append(orders.pop())                      # 현재 실어야 하는 순서가 나올때까지 보조로 옮겨줌

        if not orders:                                      # 만약 컨테이너 벨트가 상자가 하나도 안남는다면
            break                                           # 더 이상 상자를 실을 수 없으므로 반복 종료

        orders.pop()                                        # 실어야 하는 상자를 찾았다면 실어줌
        answer += 1
    return answer


# print(solution([4, 3, 1, 2, 5]))
