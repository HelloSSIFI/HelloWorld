def solution(word):
    word = list(word)
    pre = list()

    for i in range(len(word)):
        if pre and pre[-1] == word[i]:
            pre.pop()
        else:
            pre += word[i]
    else:
        if pre:return 0
        return 1

print(solution('baabaa'))


def solution(word):
    # 시간초과 코드

    while len(word) > 1:
        idx = 0
        pre = ''
        while idx < len(word)-1:
            if word[idx] == word[idx+1]:
                idx += 2
                pass
            else:
                pre += word[idx]
                idx += 1


        else:
            word = pre


    else:
        if len(word):
            return 0
        return 1
