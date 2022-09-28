from collections import defaultdict, deque


def bfs(a, b, n, tower):
    cnt = 1
    visited = [0] * (n+1)    # 방문 체크
    visited[a] = 1
    q = deque()
    q.append(a)

    while q:
        t = q.popleft()

        for i in tower[t]:
            if visited[i] or i == b:    # 방문했거나 끊어진 부분은 방문하지 않는다
                continue
            cnt += 1    # 연결 갯수 카운트
            q.append(i)    # 다음 이동할 곳 추가
            visited[i] = 1    # 방문 체크

    return cnt


def solution(n, wires):
    answer = 100
    tower = defaultdict(list)
    for a, b in wires:
        tower[a].append(b)
        tower[b].append(a)

    for a, b in wires:
        temp = bfs(a, b, n, tower)
        answer = min(answer, abs(temp - (n - temp)))    # answer와 두 전력망 차이 비교해서 더 작은 값 answer에 저장

    return answer