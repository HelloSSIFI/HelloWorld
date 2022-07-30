from collections import deque


T = int(input())
answer = []
for t in range(T):
    K, M, P = map(int, input().split())
    check = [0] * (M+1)
    strahler = [[0, 0]] * (M+1)
    graph = [[] for _ in range(M+1)]
    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        check[b] += 1

    q = deque()
    for i in range(1, M+1):
        if check[i] == 0:
            q.append(i)
            strahler[i] = [1, 1]

    while q:
        now = q.popleft()

        if strahler[now][1] >= 2:
            strahler[now][0] += 1

        for i in graph[now]:
            check[i] -= 1
            if strahler[i][0] == strahler[now][0]:
                strahler[i][1] += 1
            elif strahler[i][0] < strahler[now][0]:
                strahler[i] = [strahler[now][0], 1]

            if check[i] == 0:
                q.append(i)

    answer.append('{} {}\n'.format(K, strahler[M][0]))

print(''.join(answer))