from collections import deque

def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    for i in range(n-1):
        a, b = wires[i]
        tree[a].append(b)
        tree[b].append(a)

    answer = float('inf')

    edges = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # 1번부터 n번까지 트리를 돌면서
    for j in range(1, n+1):

        # 해당 노드의 간선을 하나씩 제거해보면서 순회
        for k in range(len(tree[j])):
            tmp = tree[j][k]

            # 제거해보지 않은 간선이라면 실행
            if edges[j][tmp] == 0 and edges[tmp][j] == 0:
                edges[j][tmp], edges[tmp][j] = 1, 1

                # 현재 노드와 연결된 노드들을 순회하면서 갯수를 셈
                visit, cnt = [0 for _ in range(n+1)], 0
                visit[j] = 1
                Q = deque([j])

                while Q:
                    now = Q.popleft()
                    cnt += 1

                    for x in tree[now]:
                        if visit[x] == 0 and {tmp, j} != {now, x}:
                            visit[x] = 1
                            Q.append(x)

                answer = min(answer, abs(abs(n-cnt) - cnt))
    return answer

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))