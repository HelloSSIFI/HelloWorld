from collections import deque


def solution(p):
    if not p:return p               # 빈 문자열이면 그대로 return

    def check(word):
        queue = deque([])

        for w in word:
            if w == '(':
                queue.append(w)
            else:
                if not queue:
                    return False
                queue.pop()

        return True


    def divide(word):
        l, r, = 0, 0
        for i in range(len(word)):
            if word[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                return word[:i+1], word[i+1:]

    u, v = divide(p)
    if check(u):
        return u + solution(v)

    else:
        ans = '(' + solution(v) + ')'

        for tmp in u[1:len(u)-1]:
            ans += ')' if tmp == '(' else '('

        return ans


print(solution(")("))