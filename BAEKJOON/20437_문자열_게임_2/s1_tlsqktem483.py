import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    w = input().rstrip()
    k = int(input())
    char_count = defaultdict(int)
    char_idx = defaultdict(list)
    check = []

    for i in range(len(w)):
        c = w[i]
        char_count[c] += 1
        char_idx[c].append(i)

    min_v = float('inf')
    max_v = 0
    for s in char_count.keys():
        if char_count[s] >= k:
            i, j = 0, k-1
            while j < char_count[s]:
                l, r = char_idx[s][i], char_idx[s][j]
                min_v = min(min_v, r-l+1)
                max_v = max(max_v, r-l+1)
                i += 1
                j += 1
    print(min_v, max_v) if max_v else print(-1)
