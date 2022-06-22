import sys

n, k = map(int, sys.stdin.readline().split())
c = [int(sys.stdin.readline()) for _ in range(n)]

ans = [100001] * (k+1)
ans[0] = 0

c.sort()
for coin in c:
    for i in range(coin, k+1):
        ans[i] = min(ans[i], ans[i-coin] + 1)

print(ans[-1] if ans[-1] != 100001 else -1)