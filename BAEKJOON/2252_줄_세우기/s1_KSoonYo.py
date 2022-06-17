# fail -> 시간초과

import sys
from collections import deque
input = sys.stdin.readline

q1 = deque()
q2 = deque()

N, M = map(int, input().split())

for _ in range(M):
    A, B = map(int, input().split())

    q1.append(A)
    q1.append(B)

while q1:
    temp = q1.popleft()
    
    if temp in q1:
        continue
    
    q2.append(temp)


print(*q2)

