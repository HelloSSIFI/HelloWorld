import heapq

def solution(N, road, K):
    answer = 0
    lines = [[] for _ in range(N)]
    for a, b, c in road:                                        # 인접리스트 형식으로 마을 정보를 넣어줌
        lines[a - 1].append((b - 1, c))
        lines[b - 1].append((a - 1 ,c))
    visited = [0] * N
    heap = [(0, 0)]
    while heap and heap[0][0] <= K:                             # 가까운 마을부터 탐색하므로 더 이상 마을이 없거나 시간이 K를 넘어가면 탐색종료
        c, node = heapq.heappop(heap)

        if visited[node]:                                       # 이미 방문한 곳이면 다음 반복
            continue

        visited[node] = 1                                       # 현재 마을을 방문표시
        answer += 1                                             # 결과값 + 1
        for next_node, d in lines[node]:                        # 현재 마을에서 갈 수 있는 지역들 중 방문안한 지역을 힙에 넣어줌
            if not visited[next_node]:
                heapq.heappush(heap, (c + d, next_node))
    return answer


# print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
