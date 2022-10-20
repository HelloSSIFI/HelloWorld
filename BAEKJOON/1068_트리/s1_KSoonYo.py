
def dfs(tree, node, removed):
    if node == removed:                                                             # 지우려고 하는 노드라면 진입 x
        return 0

    if not tree[node]:
        return 1

    cnt = 0
    for next_node in tree[node]:
        cnt += dfs(tree, next_node, removed)
    
    # 만약 자식 노드들 중 leaf 노드가 count되지 않았다면, 현재 노드가 leaf 노드가 된다.    
    if not cnt:                                                                     
        return 1
    return cnt

N = int(input())
info = [0] + list(map(lambda x : x + 1, list(map(int, input().split()))))           # 1번부터 root 노드 시작
removed = int(input()) + 1

tree = [0] + [[] for _ in range(N)]
root = 1 
for node in range(1, N + 1):
    if not info[node]:
        # 부모 노드가 0이므로 해당 노드는 root 노드
        root = node
        continue
    parent = info[node]
    tree[parent].append(node)

print(dfs(tree, root, removed))
