import sys
sys.setrecursionlimit(10**6)


answer = 0


def dfs(graph, a, prev, now):
    global answer
    # 리프 노드인 경우
    if len(graph[now]) == 1 and graph[now][0] == prev:
        return a[now]

    check = a[now]
    for nxt in graph[now]:
        if nxt == prev:    # 부모 노드로 가는 길이면 skip
            continue
        tmp = dfs(graph, a, now, nxt)
        answer += abs(tmp)    # 이동한 가중치
        check += tmp    # 현 위치와 가중치 합산

    return check


def solution(a, edges):
    global answer

    if sum(a):    # 모두 0으로 만들지 못하는 경우
        return -1

    graph = [[] for _ in range(len(a))]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    dfs(graph, a, -1, 0)

    return answer