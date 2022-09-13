def solution(citations):
    ci = sorted(citations, reverse=True)
    n = len(ci)
    for i, c in enumerate(ci):
        if i >= c:
            return i
    return n


print(solution([3, 0, 6, 1, 5]))
print(solution([6, 5, 5, 5, 3, 2, 1, 0]))