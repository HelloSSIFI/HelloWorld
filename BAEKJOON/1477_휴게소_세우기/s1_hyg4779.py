'''
실패코드
'''

from collections import defaultdict
import heapq
n, m, k = map(int, input().split())

spots = sorted(list(map(int, input().split())))

idx = defaultdict(list)
dist = []

# 시작 지점과 첫 지점 입력
idx[0-spots[0]].append((0, spots[0]))
heapq.heappush(dist, 0-spots[0])

for i in range(1, n):
    # l: 왼쪽 위치, r: 오른쪽 위치
    l, r = spots[i-1], spots[i]
    # 해당 거리차를 가진 위치들 담음
    idx[l-r].append((l, r))
    #
    heapq.heappush(dist, l-r)

# 끝 지점과 종점 입력
idx[spots[-1]-k].append((spots[-1], k))
heapq.heappush(dist, spots[-1]-k)


while m:
    m -= 1
    now = heapq.heappop(dist)

    while idx[now]:
        l, r = idx[now].pop()
        q = (l+r)//2


        idx[l-q].append((l, q))
        idx[q-r].append((q, r))

        heapq.heappush(dist, (l-q))
        heapq.heappush(dist, (q-r))

print(heapq.heappop(dist)*(-1))