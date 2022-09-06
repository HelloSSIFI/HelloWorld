import heapq


def solution(n, paths, gates, summits):
    if len(gates) > len(summits):                               # 출입구에서 봉우리로 갈 때 최소 intensity가 나온다면
        start_node = set(summits)                               # 돌아올 때는 갈 때와 같은 경로로 오면 되기 때문에
        middle_node = set(gates)                                # 단방향만 찾아주면 됨
    else:                                                       # 반복을 적게 돌기 위해 시작점과 산봉우리 중 작은것을 택하고
        start_node = set(gates)                                 # 편도 길이만 찾아줌
        middle_node = set(summits)

    lines = [[] for _ in range(n + 1)]
    for s, e, w in paths:                                       # 인접 리스트 방식으로 간선 저장
        lines[s].append((e, w))
        lines[e].append((s, w))

    candi = []                                                  # 각각의 스타트 지점에서의 결과값을 저장
    for s in start_node:
        visited = [0] * (n + 1)
        heap = [(0, s)]
        intensity = 0
        while heap:                                             # 프림 방식으로 각각의 노드를 찾아줌
            w, node = heapq.heappop(heap)                       # 이 때 코스 최대값이 갱신될 때마다 intensity를 갱신

            if visited[node]:
                continue
            visited[node] = 1

            intensity = max(intensity, w)
            if node in middle_node:                             # 골인 지점을 찾았다면 candi에 intensity와 해당 노드를 넣어주고 반복종료
                if gates[0] in start_node:                      # 위에서 시작지점을 출입구와 산봉우리 중 작은값으로 선택했으므로
                    candi.append((node, intensity))             # 현재 시작 지점이 출입구인지 산봉우리인지 확인하여
                else:                                           # 산봉우리 번호가 candi에 들어갈 수 있도록 맞게 넣어줌
                    candi.append((s, intensity))                # 모든 시작점에서 candi를 찾은 후 candi를 [intensity 우선, 산봉우리 차선] 오름차순 정렬하여 첫 번째 요소 출력
                break

            for next_node, next_w in lines[node]:
                if not visited[next_node] and (next_node not in start_node):
                    heapq.heappush(heap, (next_w, next_node))
    candi.sort(key=lambda x: (x[1], x[0]))

    return candi[0]


# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
