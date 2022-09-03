def solution(n, paths, gates, summits):
    answer = [0, 10000000]

    graph = [[] for _ in range(n+1)]
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])

    def dfs(now, inten, visited, check, start):
        nonlocal answer

        if check and now in gates:
            if now == start:
                if answer[1] > inten:
                    answer = [check, inten]
                elif answer[1] == inten:
                    answer = min(answer, [check, inten], key=lambda x:x[0])

            return

        for node, cost in graph[now]:
            if visited[node]:

                if check and node in summits:
                    continue

                if node in gates and node != start:
                    continue


                visited[node] -= 1
                dfs(node, max(inten, cost), visited, node if not check and node in summits else check, start)
                visited[node] += 1


    visit = [2]*(n+1)
    for summit in summits:
        visit[summit] -= 1

    for gate in gates:
        # 현재노드, 걸린 시간, 방문한 곳, 체크한 산 봉우리, 입구
        visit[gate] -= 1
        dfs(gate, 0, visit, 0, gate)

    return answer


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))