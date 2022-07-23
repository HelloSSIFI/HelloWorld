"""
다익스트라, dp
다시 풀이
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
tree = defaultdict(list)
visited = [False for _ in range(N+1)]

for _ in range(M):
    s, e, v = map(int, input().split())
    tree[s].append([e, v])
    tree[e].append([s, v])

start, end = 1, 2

print(tree)