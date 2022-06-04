S = input()
stack = []
mul = 1
result = 0

for i in range(len(S)):                     # 문자열 순회
    if S[i] == '(':                         # 여는 소괄호이면
        stack.append('(')                   # 스택에 push
        mul *= 2                            # 배수를 2 곱해줌
    
    elif S[i] == '[':                       # 여는 대괄호이면
        stack.append('[')                   # 스택에 push
        mul *= 3                            # 배수를 3 곱해줌
    
    elif S[i] == ')':                       # 닫는 소괄호이면
        if stack and stack.pop() == '(':    # 스택의 최상단이 여는 소괄호인지 확인
            if S[i - 1] == '(':             # 바로 이전 문자가 여는 소괄호이면
                result += mul               # 현재 배수를 결과에 더해줌
            mul //= 2                       # 배수를 2 나눠줌
        else:                               # 스택이랑 일치하지 않으면
            result = 0                      # 결과를 0으로 만들고 반복 종료
            break
    
    else:
        if stack and stack.pop() == '[':    # 닫는 대괄호도 마찬가지
            if S[i - 1] == '[':
                result += mul
            mul //= 3
        else:
            result = 0
            break

if stack:                                   # 반복이 끝났는대도 스택이 남아있으면
    result = 0                              # result를 0으로 만들어줌

print(result)
