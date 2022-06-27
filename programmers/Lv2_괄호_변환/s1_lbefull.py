def is_right(target_s):             # 올바른 괄호 문자열인지 판별
    stack = []
    for s in target_s:
        if not stack:               # 스택이 비었고
            if s == ')':            # 현재 문자가 ) 이면 거짓 반환
                return False
            stack.append(s)         # 아니라면 스택에 넣어줌
        
        elif s == '(':              # 현재 문자가 ( 라면
            stack.append(s)         # 스택에 넣어줌
        
        else:                       # 현재 문자가 ) 라면
            stack.pop()             # 스택에서 하나 제거
    
    if stack:                       # 반복이 끝났는데 스택이 남았다면
        return False                # 거짓 반환
    return True                     # 그 이외에는 모두 참 반환


def solution(p):
    if is_right(p):                 # 올바른 괄호 문자열이면(빈 문자열 포함)
        return p                    # 해당 문자열 반환
    
    cnt1 = 0                        # u와 v로 나눔
    cnt2 = 0                        # u는 더이상 균형잡힌 괄호 문자열로 나뉘면 안되므로
    for i in range(len(p)):         # 가장 짧게 균형잡힌 괄호 문자열이 만들어지면 해당 인덱스를 기준으로 나눔
        if p[i] == '(':             # ( 개수 카운트
            cnt1 += 1
        else:                       # ) 개수 카운트
            cnt2 += 1
        
        if cnt1 == cnt2:            # 만약 ( 와 ) 개수가 같다면
            break                   # 반복 종료
    
    u = p[:i + 1]                   # 인덱스 i를 기준으로 문자열을 나눔
    v = p[i + 1:]

    if is_right(u):                 # u가 올바른 괄호 문자열이면
        return u + solution(v)      # u뒤에 v를 재귀하여 반환
    
    new_u = ''                      # u가 올바른 괄호 문자열이 아니라면
    for s in u[1:-1]:               # u의 첫 번째와 마지막 문제를 제거하고
        if s == '(':                # 나머지 문자의 괄호 방향을 뒤집어서
            new_u += ')'            # new_u를 만들고
        else:                       # '(' + 'v로 재귀' + ')' + '뒤집은u' 반환
            new_u += '('

    return '(' + solution(v) + ')' + new_u


# print(solution("()))((()"))
