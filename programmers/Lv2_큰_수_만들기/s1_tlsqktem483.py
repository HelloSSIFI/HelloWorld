"""
tc 8, 10 시간초과
"""
def solution(number, k):
    answer = ''
    remain = k
    i = 0
    while remain > 0 and i <= len(number)-k:
        temp = list(map(int, number[i:i+remain+1]))
        ti = temp.index(max(temp))
        remain -= ti
        i += ti + 1
        answer += str(temp[ti])
        if remain <= 0:
            answer += number[i:]
        if len(number) - i == remain:
            break
    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("4321", 1))