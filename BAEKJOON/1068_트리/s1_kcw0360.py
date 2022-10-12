from collections import defaultdict
import sys
input = sys.stdin.readline


# 리프찾기(dfs로 탐색)
def leaf(node):
    result = 0
    stack = [node]

    if node in node_dict:
        while stack:
            t = stack.pop()
            if t in node_dict:
                stack.extend(node_dict[t])
            else:
                result += 1

    return result


N = int(input())    # 노드의 개수

# 부모가 없는 노드(루트): -1, 각 노드의 부모 노드가 input
node = list(map(int, input().split()))
del_node = int(input())    # 삭제할 노드 번호
node_dict = defaultdict(list)    # 부모 노드가 key, 자식 노드가 value

# 삭제할 노드번호에 맞는 dict의 key값을 없애기
# key의 value가 자식 노드기 때문에 더이상 탐색 하지 않게 됨
for i in range(N):
    if i == del_node or node[i] == del_node:
        continue
    else:
        node_dict[node[i]].append(i)

print(leaf(-1))