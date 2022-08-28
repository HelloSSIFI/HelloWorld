def solution(s):
    answer = -1
    braket = {')': '(', '}': '{', ']': '['}
    n = len(s)
    for i in range(n):
        now = s[i:]+s[:i]
        stack = []

        for j in range(n):
            if now[j] in ('(', '{', '['):
                stack.append(now[j])
            elif stack and braket[now[j]] == stack[-1]:
                stack.pop()
            else:
                break
        else:
            if stack:
                continue
            answer += 1

    return answer+1


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution('}}}'))