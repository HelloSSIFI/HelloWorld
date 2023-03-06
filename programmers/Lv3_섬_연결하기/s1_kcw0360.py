def find(graph, x):
    if graph[x] != x:
        graph[x] = find(graph, graph[x])
    return graph[x]


def union(graph, a, b):
    a = find(graph, a)
    b = find(graph, b)

    if a < b:
        graph[b] = a
    else:
        graph[a] = b


def solution(n, costs):    # 크루스칼 알고리즘
    answer = 0
    graph = [0] * (n+1)    # 부모 테이블 초기화
    for i in range(n+1):
        graph[i] = i

    costs.sort(key=lambda x: x[2])    # 비용 기준으로 오름차순 정렬

    for a, b, cost in costs:
        if find(graph, a) != find(graph, b):    # find 연산 결과가 다른 경우
            union(graph, a, b)    # union 연산을 통해 최소 신장트리에 추가
            answer += cost    # 연결 비용 추가

    return answer