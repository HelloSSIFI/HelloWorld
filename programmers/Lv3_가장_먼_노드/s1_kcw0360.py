from collections import deque

def solution(n, edge):
    visited = [0] * (n+1)    # 단방향으로 가기 위한 방문지 체크 및 1번 노드로 부터 떨어전 거리 체크
    temp = [[] for _ in range(n+1)]    # graph 생성

    for i in edge:    # graph 양방향으로 작성
        temp[i[0]].append(i[1])
        temp[i[1]].append(i[0])

    q = deque()
    q.extend(temp[1])    # 1번 노드로 부터 갈 수 있는 곳 q에 추가
    visited[1] = 1    # 출발지 체크(1번 노드부터 시작)
    cnt = 1    # 거리 카운트

    while q:
        for i in range(len(q)):    # 1번에서 갈수 있는 곳만 확인
            now = q.popleft()

            if visited[now] == 0:    # 단일 방향으로 가기 위함
                visited[now] = cnt
                q.extend(temp[now])    # 다음 갈 곳 추가

        cnt += 1    # 같은 거리에 있는 곳을 모두 확인 했다면 멀어진 노드거리 계산을 위해 cnt +1

    answer = visited.count(max(visited))    # 방문 했던 곳에서 최대 거리를 구한 후 개수 세기

    return answer

