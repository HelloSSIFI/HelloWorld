V, E = map(int,input().split())

graph = []    # 입력 받은 그래프
mst = []    # 최소 신장 트리
beta = [0]    # 상호 베타적 집합

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append([A, B, C])

graph.sort(key=lambda x: x[2])    # 가중치로 간선 정렬 (정점1, 정점2, 가중치)

for i in range(1, V+1):
    beta.append(i)    # 각 정점

def find(u):
    if u != beta[u]:
        beta[u] = find(beta[u])
    return beta[u]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    beta[r2] = r1    # r2가 r1의 부모

line = 0    # 간선 개수
mst_sum = 0    # 가중치 합

while True:
    if line == V-1:
        break

    u, v, s = graph.pop(0)

    if find(u) != find(v):
        union(u, v)
        mst.append([u, v])
        mst_sum += s
        line += 1

print(mst_sum)






