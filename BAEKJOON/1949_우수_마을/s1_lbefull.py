import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)


def dfs(par, v):
    if v != 1 and len(lines[v]) == 1:               # 리프노드라면
        return (population[v], 0)                   # 3가지 상태를 리턴
    
    temp = []
    for c in lines[v]:
        if c == par:
            continue
        temp.append(dfs(v, c))
    
    o = population[v]                               # 이번 마을을 우수 마을로 했을때 최대값을 저장할 변수
    x = 0                                           # 이번 마을을 우수 마을로 하지 않았을 때 최대값을 저장할 변수
    for i in range(len(temp)):
        o += temp[i][1]                             # 이전 마을이 우수 마을이 아닐경우를 모두 합한것을 o에 더해줌
        x += max(temp[i])                           # 이전 마을의 최대값을 선택하여 x에 더해줌

    return (o, x)


N = int(input())
population = [0] + list(map(int, input().split()))
lines = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

print(max(dfs(0, 1)))
