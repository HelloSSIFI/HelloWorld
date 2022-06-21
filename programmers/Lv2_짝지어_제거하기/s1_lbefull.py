def solution(s):
    answer = 1
    stack = []

    for char in s:
        if not stack or stack[-1] != char:          # 스택이 비었거나 현재 문자랑 다르면
            stack.append(char)                      # 현재 문자를 스택에 추가
        else:
            stack.pop()                             # 스택의 탑이 현재 문자랑 같으면 스택에서 pop
    
    if stack:                                       # 반복 후에 스택에 요소가 남았다면
        answer = 0                                  # 0을 반환

    return answer
