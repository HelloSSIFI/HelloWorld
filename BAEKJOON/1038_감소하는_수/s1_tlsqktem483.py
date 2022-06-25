import sys
from itertools import combinations

N = int(sys.stdin.readline())

ans = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        ans.append(int("".join(map(str, comb))))

ans.sort()

try:
    print(ans[N])
except:
    print(-1)