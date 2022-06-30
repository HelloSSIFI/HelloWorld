# 균형잡힌 괄호 문자열
def balance(p):
    cnt = 0   # '('의 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 괄호 문자열인지 확인
# 쌍이 맞으면 True 안맞으면 False 반환
def check(p):
    cnt = 0   # '('의 개수
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''

    # 빈문자열인 경우 빈문자열 반환
    if p == '':
        return answer

    idx = balance(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer