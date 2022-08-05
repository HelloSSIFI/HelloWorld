def solution(n, computers):
    answer = 0
    graph = {}

    def dfs(node):
        nonlocal graph
        graph[node][-1] = True

        if len(graph[node]) == 1:
            return

        for n_node in graph[node][:-1]:
            if not graph[n_node][-1]:
                dfs(n_node)

    for i in range(n):
        graph[i] = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
        graph[i].append(False)

    for node in graph.keys():
        if not graph[node][-1]:
            answer += 1
            dfs(node)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))