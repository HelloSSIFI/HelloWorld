from itertools import combinations
import sys
input = sys.stdin.readline


def dfs(cnt):
    global ans, w, l, d
    if cnt == 15:
        if w.count(0) == 6 and l.count(0) == 6 and d.count(0) == 6: ans = 1
        return
    x1, x2 = game[cnt]
    if w[x1] > 0 and l[x2] > 0:
        w[x1] -= 1
        l[x2] -= 1
        dfs(cnt + 1)
        w[x1] += 1
        l[x2] += 1
    if w[x2] > 0 and l[x1] > 0:
        w[x2] -= 1
        l[x1] -= 1
        dfs(cnt + 1)
        w[x2] += 1
        l[x1] += 1
    if d[x1] > 0 and d[x2] > 0:
        d[x1] -= 1
        d[x2] -= 1
        dfs(cnt + 1)
        d[x1] += 1
        d[x2] += 1


game = list(combinations(range(6), 2))
result = []

for i in range(4):
    a = list(map(int, input().split()))
    w, l, d = [], [], []
    for j in range(18):
        if j % 3 == 0: w.append(a[j])
        elif j % 3 == 1: d.append(a[j])
        elif j % 3 == 2: l.append(a[j])
    ans = 0
    dfs(0)
    result.append(ans)
print(*result)