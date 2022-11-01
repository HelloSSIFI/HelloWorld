def solution(info, edges):
    answer = 0

    # 노드 수
    n = len(info)

    graph = [[] for _ in range(n)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    # visit[a][b][c]: a마리 양 with b마리 늑대 with c 노드 방문 체크
    visit = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    visit[1][0][0] = 1
    info[0] = -1
    def dfs(sw, now):
        nonlocal answer

        # 현재 양이 여태까지 모은 양의 수보다 높으면 체크
        if sw[0] > answer:
            answer = sw[0]

        # 늑대 수가 더 많으면 return
        if sw[1] >= sw[0]:
            return

        for node in graph[now]:
            # print(sw, now)

            if visit[sw[0]][sw[1]][node] == 0:

                # 늑대나 양이 있는 경우
                if info[node] != -1:

                    # tmp: 현재 양 또는 늑대
                    tmp = info[node]

                    # 양이면 0에 +1, 늑대면 1에 +1
                    sw[tmp] += 1

                    # 방문처리
                    visit[sw[0]][sw[1]][node] = 1

                    # 데리고 다니니까 -1 처리
                    info[node] = -1
                    dfs(sw, node)

                    # 원래 양 또는 늑대 복구
                    info[node] = tmp

                    # 방문처리 취소
                    visit[sw[0]][sw[1]][node] = 0

                    # 데리고 다니던 양 또는 늑대 반환
                    sw[tmp] -= 1


                # 이미 데리고 다니는 경우
                else:

                    # 현재 상태 방문처리
                    visit[sw[0]][sw[1]][node] = 1
                    dfs(sw, node)
                    # 방문 처리 취소
                    visit[sw[0]][sw[1]][node] = 0

    # 첫 시작 양1마리, 늑대0마리 노드번호 0번 dfs 시작
    dfs([1, 0], 0)

    return answer