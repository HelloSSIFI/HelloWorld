import sys
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize

S = int(input())
ans = inf


def bfs():
    global ans
    q = deque()
    q.append((1, 0))
    visited = {
        (1, 0): 0
    }

    while q:
        display, clip = q.popleft()

        if display == S:
            print(visited[(display, clip)])
            break

        # 1번 옵션
        if (display, display) not in visited.keys():
            visited[(display, display)] = visited[(display, clip)] + 1
            q.append((display, display))

        # 2번 옵션
        if (display + clip, clip) not in visited.keys():
            visited[(display + clip, clip)] = visited[(display, clip)] + 1
            q.append((display + clip, clip))

        # 3번 옵션
        if (display - 1, clip) not in visited.keys():
            visited[(display-1, clip)] = visited[(display, clip)] + 1
            q.append((display-1, clip))


bfs()