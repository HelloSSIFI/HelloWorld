def solution(s):
    stack = []

    for parenthesis in s:
        if parenthesis == '(':    # 여는 괄호인 경우 stack에 추가
            stack.append(parenthesis)
        else:    # 닫는 괄호인 경우 stack이 비어있다면 올바르지 않는 괄호이기 때문에 False 리턴
            if stack:    # stack에 괄호가 있다면 올바른 괄호가 완성되므로 stack에서 마지막 괄호 제거
                stack.pop()
            else:
                return False

    # stack에 남아있는 괄호가 있다면 False, 존재하지 않는다면 올바른 괄호가 완성되므로 True 반환
    return False if stack else True