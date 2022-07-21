import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000)


def dfs(par, v):                            # 부모 노드와 현재 노드를 입력받아 현재 노드가 얼리 어답터인 경우와 아닌 경우를 반환
    if v != 1 and len(lines[v]) == 1:       # 1번(시작)노드가 아니고 리프노드라면
        return (1, 0)                       # 1, 0을 반환
    
    temp = []                               # 자식 노드들의 반환값을 저장할 리스트
    for i in lines[v]:                      # 부모 노드가 아닌 곳을 방문하여
        if i == par:                        # 반환값을 리스트에 추가
            continue
        temp.append(dfs(v, i))
    
    o = 1
    x = 0
    for i in range(len(temp)):              # 자식 노드들의 반환값중 작은 것에
        o += min(temp[i])                   # 현재 노드가 얼리 어답터인 경우를 더해주고
        x += temp[i][0]                     # 자식이 모두 얼리 어답터의 경우에 현재 노드가 아닐경우를 더해줌
    
    return (o, x)


N = int(input())
lines = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

print(min(dfs(0, 1)))                       # 1번 노드를 루트 노드로 시작
