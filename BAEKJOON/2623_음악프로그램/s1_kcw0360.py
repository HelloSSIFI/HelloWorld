from collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1):    # 담당 가수 제외
        graph[temp[i]].append(temp[i+1])
        indegree[temp[i+1]] += 1    # 진입차수 체크

q = deque()
answer = []

for i in range(1, N+1):
    if indegree[i] == 0:    # 진입차수가 0인 값 q에 추가
        q.append(i)

while q:
    now = q.popleft()
    answer.append(now)

    for i in graph[now]:
        indegree[i] -= 1    # now 값이 진입 차수인 값의 카운트 -1
        if indegree[i] == 0:    # 진입차수가 0이 되는 곳이면 q에 추가
            q.append(i)

if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)