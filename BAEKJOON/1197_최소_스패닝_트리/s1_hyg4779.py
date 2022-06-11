V, E = map(int, input().split())            # V: 정점 개수, E: 간선 개수
'''
kruskal 알고리즘
find 부모노드 찾기
union 이어주기
'''
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

base = list(range(V+1))


def find(v):
    if v == base[v]:
        return v
    base[v] = find(base[v])
    return base[v]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        base[a] = b
    else:
        base[b] = a


ans = 0
for s, e, w in edges:
    if find(s) != find(e):
        union(s, e)
        ans += w

print(ans)