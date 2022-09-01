# 백트래킹을 해도 방문했던 노드의 자식 노드를 다음에 방문할 노드로 추가하는 것이 핵심

def dfs(tree, info, node, candidates, sheep = 1, wolf = 0):
    global answer 
    candidates = [candidate for candidate in candidates if candidate != node] + tree[node] 
    
    if sheep <= wolf or not candidates:
        answer = max(answer, sheep)
        return
    
    for next_node in candidates:
        # 다음 노드에 양이 있는 경우
        if info[next_node] == 0:
            dfs(tree, info, next_node, candidates, sheep + 1, wolf)
        
        # 다음 노드에 늑대가 있는 경우
        else:
            dfs(tree, info, next_node, candidates, sheep, wolf + 1)
        

    return 




def solution(info, edges):
    global answer 
    answer = 0
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        s, e = edge
        tree[s].append(e)
    dfs(tree, info, 0, [])
    return answer