def solution(s):
    answer = [0, 0]
    c = s.count('1')
    answer[0] += 1
    answer[1] += len(s) - c
    while c != 1:
        s = bin(c)[2:]
        c = s.count('1')
        answer[0] += 1
        answer[1] += len(s) - c

    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))