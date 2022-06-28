def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    max_sheep = 0

    for edge in edges:
        graph[edge[0]].append(edge[1])

    def dfs(idx, sheep, wolf, next_node):
        nonlocal max_sheep

        max_sheep = max(max_sheep, sheep)
        next_node.update(graph[idx])
        for next in next_node:
            if info[next]:
                if sheep != wolf + 1:
                    dfs(next, sheep, wolf+1, next_node-{next})
            else:
                dfs(next, sheep+1, wolf, next_node-{next})
    dfs(0, 1, 0, set())
    return max_sheep


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))