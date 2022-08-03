import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())                        # N : 현재 수빈이가 있는 위치, K : 동생이 있는 위치
q = deque([(0, N)])                                     # (현재 시간, 현재 위치)

time_table = [0] * 100001                               # 인덱스: 현재 위치, 값: 방문한 시간
count_table = [0] * 100001                              # 인덱스: 현재 시간, 값: 방문한 횟수
minT = 987654321
while q:
    t, X = q.popleft()
    
    if X == K:                                          # 동생 위치까지 도달했다면
        count_table[t] += 1                             # 현재 시간에 count + 1
        minT = min(minT, t)                             # 동생 위치까지 도달하는 데 가장 빠른 시간 갱신
        continue

    for next in [X - 1, X + 1, X * 2]:
        if 0 <= next <= 100000 and (not time_table[next] or (t + 1) <= time_table[next]):   # 인덱스 범위이면서 다음 위치에 방문한 적이 없거나 이전에 방문했던 시간보다 빠르거나 같은 시간에 도달한다면
            time_table[next] = t + 1                                                        # 다음 위치 방문, 방문 시간 갱신
            q.append((t + 1, next))                                                     

print(minT)
print(count_table[minT])