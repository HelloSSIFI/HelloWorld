import sys
input = sys.stdin.readline


N = int(input())

arr = [0]*(N+1)
edges = []

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1
    edges.append([a, b])

d, g = 0, 0

for i in range(1, N+1):
    if arr[i] >= 3:    # ㅈ은 3개 이상 연결된 노드로만 가능
        g += arr[i] * (arr[i] - 1) * (arr[i] - 2) // 6    # 해당 노드에서 연결된 노드 3개 선택(nC3)

for a, b in edges:
    d += (arr[a] - 1) * (arr[b] - 1)    # 연결된 a,b의 노드에 각각 두개 이상 연결된 노드가 있어야 하나의 ㄷ모양이 생성

if d > 3*g:
    print("D")
elif d < 3*g:
    print("G")
else:
    print("DUDUDUNGA")