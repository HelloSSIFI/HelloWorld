import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visit = set()       # 방문한 노드
adopt = set()       # 얼리어답터 노드


def dfs(n):

    # 방문 처리
    visit.add(n)
    # 단일 노드면 return
    if len(graph[n])<=1:
        return True

    # 단일 노드가 아닐 때
    for i in graph[n]:
        # 방문하지 않은 곳만
        if i not in visit:
            # 연결된 노드가 단일 노드라면 현재 노드를 어답터에 추가
            if dfs(i):
                adopt.add(n)
            # 연결된 노드가 단일 노드가 아닌데 어답터에 없다면 현재 노드를 추가
            elif not i in adopt:
                adopt.add(n)
    return False


for i, start in enumerate(graph):
    # 무조건 여러 노드와 연결된 곳에서 시작
    if len(start)>1:
        dfs(i)
        break

# 노드가 두개밖에 없다면 프린트1
if N==2:
    print(1)
else:
    print(len(adopt))

