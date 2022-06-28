from collections import deque


def solution(p):
    if not p:return p               # 빈 문자열이면 그대로 return

    def check(word):                # 검사하는 함수
        queue = deque([])

        for w in word:              # 열린 괄호 무조건 append
            if w == '(':
                queue.append(w)
            else:                   # 닫힌 괄호일 때
                if not queue:       # 열린 괄호 없으면 잘못된 괄호열
                    return False
                queue.pop()         # 열린 괄호 pop

        return True


    def divide(word):                               # u, v 나누는 함수
        l, r, = 0, 0
        for i in range(len(word)):                  # 열린 괄호 닫힌 괄호 숫자 세기
            if word[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:                              # 서로 같은 수일 때 나눠서 return
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