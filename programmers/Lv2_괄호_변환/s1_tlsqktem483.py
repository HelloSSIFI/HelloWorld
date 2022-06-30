def check(s):
    temp = 0
    for c in s:
        if c == '(':
            temp += 1
        else:
            temp -= 1

        if temp < 0:
            return False
    return True


def change(s):
    if s == '':
        return ''

    u, v = '', ''
    opened, closed = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            opened += 1
        else:
            closed += 1
        if opened == closed:
            u, v = s[:i+1], s[i+1:]
            break

    if check(u):
        return u + change(v)
    else:
        temp = '(' + change(v) + ')'
        for j in u[1:-1]:
            if j == '(':
                temp += ')'
            else:
                temp += '('
        return temp


def solution(p):
    chk = check(p)

    if chk:
        return p
    else:
        return change(p)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))