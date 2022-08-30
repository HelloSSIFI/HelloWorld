from collections import defaultdict, deque

def solution(N, road, K):
    info = defaultdict(list)
    visited = [-1] + [0] * N
    for a, b, c in road:    # 해당 마을에서 갈 수 있는 마을과 시간을 같이 저장(양방향)
        info[a] += [[b, c]]
        info[b] += [[a, c]]

    q = deque()
    q.append([1, 0])
    visited[1] = 1    # 1번마을에서 배달이 이루어지기 때문에 1번 마을도 배달 가능지역으로 체크
    while q:
        town, time = q.popleft()    # 현재 마을, 1번 부터 현재 마을까지 오는데 걸린 시간

        for b, c in info[town]:
            temp = time + c
            if temp <= K and (visited[b] == 0 or temp <= visited[b]):    # 시간이 K보다 작고 방문하지 않았거나 체크가 되어있더라도 더 빠른 시간으로 올 수 있는 경우
                q.append([b, temp])
                visited[b] = temp

    return N - visited.count(0)    # 0은 배달 갈 수 없는 마을이기 때문에 카운트해서 빼준다.