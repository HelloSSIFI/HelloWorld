"""
Recursion Limit 풀지 않으면 4개의 케이스에서 런타임 에러
"""
import sys
sys.setrecursionlimit(300000)


def solution(a, edges):
    """
     DFS 활용한 풀이 : 노드의 값 중첩 및 cnt 변수 업데이트
    """
    if sum(a):
        return -1

    def dfs(node):
        nonlocal cnt, visited

        v = a[node]

        for next_node in n_list[node]:
            if not visited[next_node]:
                visited[next_node] = True
                v += dfs(next_node)

        cnt += abs(v)

        return v

    cnt = 0
    n_list = [[] for _ in range(len(a))]
    visited = [False] * len(a)

    for s, e in edges:
        n_list[s].append(e)
        n_list[e].append(s)

    visited[0] = True
    dfs(0)
    return cnt


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0, 1, 0], [[0,1],[1,2]]))