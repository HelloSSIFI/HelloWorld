"""
투포인터 풀이
"""
from collections import Counter


def solution(gems):
    answer = []
    n = len(gems)
    m = len(set(gems))

    start = 0
    cnt = Counter()

    for end in range(n):
        cnt[gems[end]] += 1
        end += 1

        while len(cnt) == m:
            cnt[gems[start]] -= 1
            if cnt[gems[start]] == 0:
                del cnt[gems[start]]
            start += 1
            answer.append([start, end])

    return sorted(answer, key=lambda x: (x[1]-x[0], x[0]))[0]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))