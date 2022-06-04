blanks = list(input())

blank_stack = []
temp = 1
result = 0

error = False
for idx in range(len(blanks)):
    if blanks[idx] == '(':
        blank_stack.append(blanks[idx])
        temp *= 2
    elif blanks[idx] == '[':
        blank_stack.append(blanks[idx])
        temp *= 3
    
    if blanks[idx] == ')':
        # 잘못된 입력인 경우를 체크
        # 1) 스택이 비어있는데 닫는 괄호를 만날 경우
        # 2) 닫는 괄호와 stack의 top이 가리키는 괄호 쌍이 맞지 않은 경우
        if not blank_stack or blank_stack[-1] == '[':
            error = True
            break

        elif blanks[idx - 1] == '(':    # 여는 괄호를 만날 때마다 미리 곱을 해줬기 때문에 직전 괄호가 같은 쌍인 경우에만 결과값에 더해준다.
            result += temp
        blank_stack.pop()
        temp //= 2   # 여는 괄호를 만날 때마다 미리 곱을 해줬기 때문에 같은 depth의 다른 모양의 여는 괄호형 계산을 위해 이전 값으로 되돌려준다.

    elif blanks[idx] == ']':
        if not blank_stack or blank_stack[-1] == '(':
            error = True
            break
        elif blanks[idx - 1] == '[':
            result += temp
        blank_stack.pop()
        temp //= 3

if blank_stack or error:
    print(0)
else:
    print(result)
    
