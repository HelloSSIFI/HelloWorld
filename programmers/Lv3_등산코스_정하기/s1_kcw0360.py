from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = [0, 10000001]
    mt = defaultdict(list)    # 길 정보
    for a, b, c in paths:
        mt[a].append([b, c])
        mt[b].append((a, c))

    q = []
    visited = [10000001] * (n+1)    # 방문지 체크, 주어진 조건 최대값을 각 위치에 저장
    for gate in gates:
        q.append([gate, 0])    # [gate, intensity]
        visited[gate] = 0    # 출입구 방문 체크

    while q:
        now, intensity = q.pop()

        # 산봉우리에 도착하거나 intensity가 더 큰 지점은 더 이상 이동하지 않는다.
        if (now in summits) or (intensity > visited[now]):
            continue

        for nxt, time in mt[now]:    # 현 위치에서 갈 수 있는 곳 찾기
            temp = max(intensity, time)    # 다음 위치와 현 위치 중 시간이 큰 것을 temp에 저장

            # temp보다 작은 경우는 지나온 길이기 때문에 체크하지 않는다.
            if temp < visited[nxt]:
                visited[nxt] = temp
                q.append([nxt, temp])

    for summit in summits:
        if visited[summit] < answer[1]:
            answer = [summit, visited[summit]]

    return answer


print(solution(	7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))

