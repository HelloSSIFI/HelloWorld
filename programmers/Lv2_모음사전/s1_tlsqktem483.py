def solution(word):
    words = ["A", "E", "I", "O", "U"]
    cnt = 0
    ans = 0

    def dfs(s):
        nonlocal cnt, ans
        if len(s) == 5:
            return
        else:
            for w in words:
                temp = s + w
                cnt += 1
                if temp == word:
                    ans = cnt
                    break
                dfs(temp)
    dfs('')
    return ans


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))