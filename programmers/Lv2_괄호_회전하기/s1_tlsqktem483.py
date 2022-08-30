def solution(s):
    answer = 0

    def check(sentence):
        a = []
        c_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in sentence:
            if c in c_dict.values():
                a.append(c)
            elif c in c_dict.keys() and (not a or a[-1] != c_dict[c]):
                return False
            else:
                a.pop()

        if a:
            return False
        return True

    for i in range(len(s)):
        if i:
            sentence = s[i:] + s[0:i]
        else:
            sentence = s[:]
        if check(sentence):
            answer += 1

    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
print(solution("()("))
print(solution("("))