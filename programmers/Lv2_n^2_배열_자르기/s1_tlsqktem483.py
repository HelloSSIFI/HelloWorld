"""
시간복잡도 : O(n**2)
런타임에러
"""
def solution(n, left, right):
    graph = [0] * (n**2)
    p = -1
    for i in range(len(graph)):
        remain = i % n
        if remain == 0:
            p += 1
        if remain <= p:
            graph[i] = p + 1
        else:
            graph[i] = remain + 1

    return graph[left:right+1]


print(solution(3, 2, 5))
print(solution(4, 7, 14))