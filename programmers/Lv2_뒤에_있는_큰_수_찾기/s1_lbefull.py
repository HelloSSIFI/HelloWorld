def solution(numbers):
    N = len(numbers)
    answer = []
    stack = []
    for i in range(N - 1, -1, -1):                      # 뒤에 있는 숫자부터 탐색
        while stack and stack[-1] <= numbers[i]:        # stack이 있고 stack의 top이 현재 숫자보다 작으면
            stack.pop()                                 # stack에서 pop

        if not stack:                                   # 스택이 비었다면 오른쪽에 큰 수가 없는 것이므로
            answer.append(-1)                           # -1 추가

        else:                                           # 비어있지 않다면
            answer.append(stack[-1])                    # stack의 top을 추가

        stack.append(numbers[i])                        # 현재 숫자를 stack에 넣고 반복

    answer.reverse()                                    # 거꾸로 탐색했으므로 리스트를 뒤집어줌
    return answer


# print(solution([2, 3, 3, 5]))
