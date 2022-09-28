import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    s, e = map(int, input().split())
    q.append((s, e))

q.sort()

c = []
heapq.heappush(c, q[0][1])

for i in range(1, N):
    if q[i][0] < c[0]:
        heapq.heappush(c, q[i][1])
    else:
        heapq.heappop(c)
        heapq.heappush(c, q[i][1])

print(len(c))