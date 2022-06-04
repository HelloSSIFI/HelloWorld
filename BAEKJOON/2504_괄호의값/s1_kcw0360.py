bracket = list(input())    # 괄호열
stack = []    # 괄호열 임시 저장
result = 0    # 결과값
temp = 1    # 임시저장값

if len(bracket) % 2:    # 괄호는 열고 닫기 때문에 항상 짝수 길이
    print(0)
    exit(0)

for idx, val in enumerate(bracket):
    # 열린 괄호에서는 temp에 해당 값을 곱하고 stack에 저장
    if val == '(':
        stack.append(val)
        temp *= 2
    elif val == '[':
        stack.append(val)
        temp *= 3

    # 닫히는 괄호는 케이스를 나눈다.
    # 이전 괄호가 짝이 다르거나 stack에 저장된 것이 없을 땐 짝이 맞지 않기 때문에 result = 0이고 반복문을 빠져나온다.
    # stack 마지막 값이 현재 val과 짝이 맞는 괄호면 result에 저장된 temp를 더하고, stack에서 여는괄호 제거 및 해당괄호 값에 대해 temp에서 나눠준다.
    elif val == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        else:
            if bracket[idx-1] == '(':
                result += temp
            stack.pop()
            temp //= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        else:
            if bracket[idx-1] == '[':
                result += temp
            stack.pop()
            temp //= 3
print(result)
