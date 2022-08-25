"""
시간초과
"""
def solution(gems):
    answer = []
    n = len(gems)
    set_gems = list(set(gems))
    m = len(set_gems)

    for i in range(n):
        start = i
        temp = []

        for j in range(i, n):
            end = j
            if gems[j] not in temp:
                temp.append(gems[j])

            if len(temp) == m:
                answer.append([start+1, end+1])
                break

    dist = n + 1
    start, end = 0, 0
    for [i, j] in answer:
        if dist > (j - i) + 1:
            dist = (j - i) + 1
            start, end = i, j

    return [start, end]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))