"""
combination 풀이
시간초과
"""
import sys
from itertools import combinations
n, k = map(int, sys.stdin.readline().split())
c = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp <= k:
        c.append(temp)

ans = []

for i in range(1, n+1):
    for comb in combinations(c, i):
        if k % sum(comb) == 0:
            ans.append(k // sum(comb))

if ans:
    print(min(ans))
else:
    print(-1)