from collections import deque


def check(s):
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            
            if (char == ')' and stack[-1] == '(') or (char == '}' and stack[-1] == '{') or (char == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False

    if stack:
        return False            
    return True



def solution(s):
    answer = 0

    if check(s):
        answer += 1

    origin = s
    while True:
        # 회전
        s = deque(s)
        elem = s.popleft()
        s.append(elem)
        s = ''.join(s)

        if s == origin:
            break

        # 문자열 검증
        elif check(s):
            answer += 1

    
    return answer

