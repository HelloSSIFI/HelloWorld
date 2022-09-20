import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set(input() for _ in range(N))
ans = 0

for _ in range(M):
    c = input()
    if c in s:
        ans += 1
print(ans)
