n = int(input())

# 모든 인구수
people = 0
graph = []

for _ in range(n):
    pos, num = map(int, input().split())
    people += num
    graph.append([pos, num])

graph.sort(key=lambda x:x[0])

# 번호가 낮은 순서부터 인구를 더하며
# 절반이 넘는 부분에서 break
cnt = 0
for i in range(n):

    cnt += graph[i][1]

    if cnt >= people/2:
        print(graph[i][0])
        break