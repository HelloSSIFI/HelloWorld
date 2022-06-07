"""
크루스칼 알고리즘
+ union-find 알고리즘
4320ms
"""
v, e = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(e)]
# cost 로 오름차순 정렬
graph.sort(key=lambda x: x[2])
parent = [0] * (v+1)
mst = []
mst_value = 0

# 부모를 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


def find(parent, x):
    """
    특정 원소의 집합 검색
    :param parent:
    :param x: 현재 노드
    :return: 루트 노드
    """
    # 루트노드를 찾을때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    """
    두 원소가 속한 집합의 결합
    """
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for (a, b, c) in graph:
    """
    사이클 판별법
    1. 두 노드의 루트노드 확인
    1.a. 루트노드가 서로 다르면 union(결합) 수행
    1.b. 루트노드가 서로 같으면 사이클 발생으로 스킵
    2. 모든 간선에 대해 반복
    """
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        mst_value += c

print(mst_value)

