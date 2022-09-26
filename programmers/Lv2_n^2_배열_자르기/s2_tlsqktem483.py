def solution(n, left, right):
    graph = []
    for i in range(left, right+1):
        q, r = i // n, i % n
        if r > q:
            graph.append(r+1)
        else:
            graph.append(q+1)
    return graph


print(solution(3, 2, 5))
print(solution(4, 7, 14))