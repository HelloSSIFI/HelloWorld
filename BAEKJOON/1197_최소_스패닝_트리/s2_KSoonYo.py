# 크루스칼 알고리즘을 이용한 최소 스패닝 트리 구성

V, E = map(int, input().split())                
 
graph = []
rep = [0] * (V + 1)
for i in range(1, V + 1):
    rep[i] = i

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph.append((start, end, weight))
graph.sort(key=lambda x : x[2])


def find(u):
    if u != rep[u]:
        rep[u] = find(rep[u])
    return rep[u]


def union(u, v):
    root1 = find(u)
    root2 = find(v)
    rep[root2] = root1

cost = 0
for connect in graph:
    u, v, w = connect
    if find(u) != find(v):
        union(u, v)
        cost += w

print(cost)



