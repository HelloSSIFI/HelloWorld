def remove(now):
    # 없어진 노드 처리
    tree[now] = -2

    # 현재 없어진 노드를 부모 노드로 하는 노드 탐색
    # dfs로 돌면서 제거처리
    for i in range(n):
        if now == tree[i]:
            remove(i)

n = int(input())
tree = list(map(int, input().split()))
v = int(input())

remove(v)
answer = 0
# 제거되지 않았고,
# 현재 노드 번호가 tree에 없다 == 부모노드가 아니다 == 자식노드가 없다 => +1
for i in range(n):
    if tree[i] != -2 and i not in tree:
        answer += 1

print(answer)