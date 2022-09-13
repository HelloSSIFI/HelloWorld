def solution(number, k):
    ans = []

    for n in number:
        while k > 0 and ans and ans[-1] < n:
            ans.pop()
            k -= 1
        ans.append(n)
    return ''.join(ans[:len(ans) - k])


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("4321", 1))