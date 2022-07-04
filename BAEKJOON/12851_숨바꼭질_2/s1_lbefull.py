from collections import deque

N, K = map(int, input().split())
visited = [[0, 100001] for _ in range(100001)]                  # 방문 방법 수, 방문 시간을 저장
visited[N] = [1, 1]
Q = deque()
Q.append((N, 1))                                                # 위치, 방문 시간을 Q에 넣을 예정

while Q:
    pos, sec = Q.popleft()

    for p in [pos + 1, pos - 1, pos * 2]:                       # 3가지 이동 방법 순회
        if 0 <= p < 100001 and sec + 1 <= visited[p][1]:        # 인덱스 범위 내에 있고 방문 시간이 같거나 작다면
            if not visited[p][0]:                               # 방문하지 않았을 경우 Q에 enQ
                Q.append((p, sec + 1))
            
            visited[p][0] += visited[pos][0]                    # 방문 방법 수에 현재 위치 방문 수를 더해주고
            visited[p][1] = sec + 1                             # 방문 시간을 현재 시간 + 1 로 맞춰줌

print(visited[K][1] - 1)
print(visited[K][0])
