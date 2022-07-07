from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    operation_dict = {
        '+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '*' : lambda x, y : x * y
    }

    operation_set = set()
    expression_call = []
    temp = ''
    for char in expression:
        if not char.isdigit():
            operation_set.add(char)
            expression_call.append(int(temp))
            expression_call.append(char)
            temp = ''
            continue
        temp += char
    expression_call.append(int(temp))

    priority_list = list(permutations(operation_set))
    maxV = 0       
    for priority in priority_list:
        isp = {}
        for op_i in range(len(priority)- 1, -1, -1):
            isp[priority[op_i]] = op_i                              # 스택 내부 우선순위 정의
        
        new_expression = []                                         # 중위 표현식 -> 후위 표현식
        op_stack = []
        for expression in expression_call:                   
            if expression not in operation_set:
                new_expression.append(expression)
                continue
            
            if not op_stack or isp[op_stack[-1]] < isp[expression]:
                op_stack.append(expression)
                continue
            
            while op_stack and isp[op_stack[-1]] >= isp[expression]:
                top = op_stack.pop()
                new_expression.append(top)
            op_stack.append(expression)
        
        while op_stack:
            new_expression.append(op_stack.pop())

        stack = []                                                  # 후위 표현식 값을 저장할 stack
        top = -1
        for temp in new_expression:
            if temp not in operation_set:
                stack.append(temp)
                top += 1
                continue

            stack[top - 1] = operation_dict[temp](stack[top - 1], stack[top])
            stack.pop()
            top -= 1
        maxV = max(maxV, abs(stack[-1]))
    answer = maxV
    return answer

print(solution('100-200*300-500+20'))
