def solution(order):
    answer = 0
    new_order = [0] * len(order)                        # 현재 상자가 몇번째로 트럭에 실려야 하는지 저장
    for i in range(len(order)):
        new_order[order[i] - 1] = i
    
    new_order = new_order[::-1]                         # 리스트의 마지막부터 확인하도록 뒤집음
    stack = []                                          # 보조 컨테이너 벨트에 들어갈 상자를 저장할 스택
    while stack or new_order:                           # 둘 다 빌때까지 반복
        if new_order and answer == new_order[-1]:       # 만약 컨테이너 벨트의 상자가 현재 트럭에 실어야하는 순서라면
            answer += 1                                 # 실어줌
            new_order.pop()
            continue
        
        if stack and answer == stack[-1]:               # 보조 컨테이너 벨트 상자가 현재 순서라면
            answer += 1                                 # 실어줌
            stack.pop()
            continue
        
        if not new_order:                               # 컨테이너 벨트는 비었는데 보조 컨테이너 순서가 아니라면
            break                                       # 반복 종료

        stack.append(new_order.pop())                   # 위의 경우가 아니라면 보조 컨테이너로 상자를 옮겨줌
    return answer


# print(solution([4, 3, 1, 2, 5]))
