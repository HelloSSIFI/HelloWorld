def making(word):
    if not word: return False
    return [word[i-1:i+1].upper() for i in range(1, len(word)) if word[i-1].isalpha() and word[i].isalpha()]


def solution(str1, str2):
    pre = making(str1)
    post = making(str2)

    cross = set(pre) & set(post)
    all = set(pre) | set(post)

    if not all: return 65536
    cross_val = all_val = 0

    for el in cross:
        cross_val += min(pre.count(el), post.count(el))

    for al in all:
        all_val += max(post.count(al), pre.count(al))

    return int(cross_val/all_val*65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
