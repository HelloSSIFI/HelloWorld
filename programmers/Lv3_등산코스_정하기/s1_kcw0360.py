from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    answer = []
    summits = set(summits)    # 중복 제거
    mt = defaultdict(list)    # 길 정보
    for a, b, c in paths:    # 양방향으로 길 정보 저장
        mt[a].append([b, c])
        mt[b].append((a, c))

    q = []
    visited = [10000001] * (n+1)    # 방문지 체크, 주어진 조건 최대값을 각 위치에 저장
    for gate in gates:
        heapq.heappush(q, [gate, 0])    # [gate, intensity]
        visited[gate] = 0    # 출입구 방문 체크

    while q:
        now, intensity = heapq.heappop(q)

        # 산봉우리에 도착하거나 intensity가 더 큰 지점은 더 이상 이동하지 않는다.
        if (now in summits) or (intensity > visited[now]):
            continue

        for nxt, time in mt[now]:    # 현 위치에서 갈 수 있는 곳 찾기
            temp = max(intensity, time)    # 다음 위치와 현 위치 중 시간이 큰 것을 temp에 저장
            # temp보다 작은 경우는 지나온 길이기 때문에 체크하지 않는다.
            if temp < visited[nxt]:
                visited[nxt] = temp
                heapq.heappush(q, [nxt, temp])

    for summit in summits:
        answer.append([summit, visited[summit]])

    answer.sort(key=lambda x: (x[1], x[0]))    # 1순위 intensity, 2순위로 산봉우리 번호로 오름차순 정렬

    return answer[0]