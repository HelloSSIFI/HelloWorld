from collections import defaultdict, deque
def solution(n, wires):

    def node_count(node, exc):
        visited = [False] * (n+1)
        visited[node] = True
        q = deque()
        q.append([node, 1])
        s = 0

        while q:
            c, cnt = q.popleft()
            s += 1
            for n_node in w[c]:
                if n_node != exc and not visited[n_node]:
                    q.append([n_node, cnt+1])
                    visited[n_node] = True
        return s

    answer = float('inf')
    w = defaultdict(list)
    for v1, v2 in wires:
        w[v1].append(v2)
        w[v2].append(v1)

    for v1, v2 in wires:
        a = node_count(v1, v2)
        b = node_count(v2, v1)
        answer = min(answer, abs(a-b))

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))